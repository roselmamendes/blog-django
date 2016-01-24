from posts.models import Post


class CreationPost:
    @staticmethod
    def create_draft(title, description, text):
        Post.objects.create(
            title=title,
            description=description,
            text=text
        )
