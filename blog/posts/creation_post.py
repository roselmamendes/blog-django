from posts.models import Post


class CreationPost:
    @staticmethod
    def create_draft(title, text):
        Post.objects.create(
            title=title,
            text=text
        )
