from django.core.management import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Create update'

    def handle(self, *args, **options):
        user = User(name='Jack', email='capitan@email.ru', password='secret', age=25)
        ...
        user.save()
        self.stdout.write(f' {user}')
