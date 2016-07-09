from __future__ import unicode_literals

from django.db import models
import subprocess
# Create your models here.
class Amazon_Url(models.Model):
	amazon_url = models.URLField(max_length=100)

	def fun(self,url):
		

		# Define command and arguments
		command = 'Rscript'
		path2script = 'specs-amazon.R'

		# Variable number of args in a list
		args = [url]

		# Build subprocess command
		cmd = [command, path2script] + args
		open('userReviews.txt', 'w').close()
		# check_output will run the command and store to result
		x = subprocess.call(cmd, universal_newlines=True)