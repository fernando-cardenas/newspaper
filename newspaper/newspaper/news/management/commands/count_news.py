from django.core.management.base import BaseCommand
from newspaper.news.models import News

class Command(BaseCommand):
    help = 'Count news.'

    def handle(self, *args, **options):
        import ipdb; ipdb.set_trace()
        print(News.objects.count())