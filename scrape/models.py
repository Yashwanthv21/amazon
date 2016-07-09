from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Amazon_Url(models.Model):
	amazon_url = models.URLField(max_length=100)
