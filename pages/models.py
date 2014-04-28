from django.db import models

# Create your models here.
class Page(models.Model):
	pageid = models.CharField(max_length = 5)
	title = models.CharField(max_length = 50)
	content = models.TextField()
