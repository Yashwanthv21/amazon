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
		args = ['http://www.amazon.in/Micromax-Bolt-S301-charger-earphone/dp/B012ACW0ZI/ref=sr_1_7?ie=UTF8&qid=1466446343&sr=8-7&keywords=celkon']

		# Build subprocess command
		cmd = [command, path2script] + args

		# check_output will run the command and store to result
		x = subprocess.call(cmd, universal_newlines=True)