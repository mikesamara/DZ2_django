from django.core.management import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'get  user by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk__lte=pk)
        self.stdout.write(f'{user}')