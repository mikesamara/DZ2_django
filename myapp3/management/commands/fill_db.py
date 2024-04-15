from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = 'fdgbioj gdafib gib dfghi adsfgi qirgp qgepih qirg  qeirgh qeirg  ergipqe rgiergbqerg iqerg qeirg qeg qergiqpgu qertkweo qeog qog qeorg '

class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=5)),
                    author=author
                )
                post.save()
