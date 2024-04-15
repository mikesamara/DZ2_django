from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **options):
        self.stdout.write("Hello world!")