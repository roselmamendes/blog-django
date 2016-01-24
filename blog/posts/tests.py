from django.test import TestCase
from posts.creation_post import CreationPost
from posts.models import Post


class CreationPostTest(TestCase):
    def test_should_create_a_new_post_with_title_and_post(self):
        CreationPost.create_draft(
            'title',
            'description',
            'long text'
        )

        posts_in_db = Post.objects.all()

        self.assertEquals(1, posts_in_db.count())

        post = posts_in_db.first()
        self.assertEqual('title', post.title)
        self.assertEqual('description', post.description)
        self.assertEqual('long text', post.text)
        self.assertIsNotNone(post.created_on)

    def test_should_description_be_optional(self):
        CreationPost.create_draft(
            'title',
             None,
            'long text'
        )

        posts_in_db = Post.objects.all()

        self.assertEquals(1, posts_in_db.count())

        post = posts_in_db.first()
        self.assertIsNotNone(post.created_on)

    # draft post
    # publish post
    # edit post
    # delete post
    # add comment
    # delete comment
    # edit comment
