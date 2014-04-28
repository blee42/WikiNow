from django.core.management.base import BaseCommand, CommandError
from pages.models import Page

class Command(BaseCommand):
	args = ''
	help = 'Process feeds for entities'

	def handle(self, *args, **options):
		for page in Page.objects.all():
			print page.title