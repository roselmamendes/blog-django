from django.utils import timezone
from posts.models import Post, Comment


class CreationPost:
    @staticmethod
    def create_draft(title, description, text, author):
        Post.objects.create(
            title=title,
            description=description,
            text=text,
            author=author
        )

    @staticmethod
    def publish(post_id):
        post_db = Post.objects.get(id=post_id)

        post_db.published_on = timezone.now()

        post_db.save(update_fields=['published_on'])

    @staticmethod
    def add_comment(post, author, comment):
        Comment.objects.create(
            post=post,
            author=author,
            text=comment
        )
