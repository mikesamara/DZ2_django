from django.core.management import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'fake users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title{j}',
                    content=f'Content{author.name} #{j} sdfsd sdf sdf sdfs w w',
                    author=author
                )
                post.save()
