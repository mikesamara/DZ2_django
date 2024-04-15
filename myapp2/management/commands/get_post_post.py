from django.core.management import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'get post  users'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author_id=pk)
        intro = f"all posts\n"
        text = "\n".join(post.content for post in posts)
        self.stdout.write(f'{intro}{text}')