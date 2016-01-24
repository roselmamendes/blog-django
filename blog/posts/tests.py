from django.test import TestCase
from posts.creation_post import CreationPost
from posts.models import Post


class CreationPostTest(TestCase):
    def test_should_create_a_new_post_with_title_and_post(self):
        CreationPost.create_draft(
            'title',
            'description',
            'long text',
            'author'
        )

        posts_in_db = Post.objects.all()

        self.assertEquals(1, posts_in_db.count())

        post = posts_in_db.first()
        self.assertEqual('title', post.title)
        self.assertEqual('description', post.description)
        self.assertEqual('long text', post.text)
        self.assertEqual('author', post.author)
        self.assertIsNotNone(post.created_on)

    def test_should_description_be_optional_on_post(self):
        CreationPost.create_draft(
            'title',
            None,
            'long text',
            'author'
        )

        posts_in_db = Post.objects.all()

        self.assertEquals(1, posts_in_db.count())

        post = posts_in_db.first()
        self.assertIsNotNone(post.created_on)

    def test_should_not_allow_save_a_post_without_required_fields(self):
        with self.assertRaises(Exception):
            CreationPost.create_draft(
                None,
                'description',
                None,
                None
            )

    def test_should_publish_a_post(self):
        CreationPost.create_draft(
            'title',
            'description',
            'long text',
            'author'
        )
        post_db = Post.objects.first()

        CreationPost.publish(post_db.id)

        post_db = Post.objects.first()

        self.assertEqual(0, post_db.comments.count())
        self.assertIsNotNone(post_db.published_on)

    def test_should_not_allow_save_a_comment_without_post_related(self):
        with self.assertRaises(Exception):
            CreationPost.add_comment(
                None,
                'author',
                'some text'
            )

    def test_should_add_a_comment_for_a_post(self):
        CreationPost.create_draft(
            'title',
            'description',
            'long text',
            'author'
        )
        post_db = Post.objects.first()
        CreationPost.publish(post_db.id)

        CreationPost.add_comment(
            post_db,
            'author of the comment',
            'commentary'
        )

        [comment_db] = CreationPost.get_comments_from_post(post_db.id)

        self.assertEqual('author of the comment', comment_db.author)
        self.assertEqual('commentary', comment_db.text)

    # draft post
    # publish post
    # edit post
    # delete post
    # add comment
    # delete comment
    # edit comment
