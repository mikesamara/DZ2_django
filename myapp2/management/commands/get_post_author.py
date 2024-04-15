from django.core.management import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'get post  users'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            intro= f" All posts of {author.name}\n"
            text='\n'.join(posts.content for posts in posts)
            self.stdout.write(f'{intro} {text}')