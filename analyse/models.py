from __future__ import unicode_literals

from django.db import models
import math
import nltk
import nltk.corpus
from nltk.text import Text
import sys
import collections
import io

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Create your models here.

class Amazon_Analyse(models.Model):
	def analyse_class(self):
		
		#start = timeit.default_timer()
		sid = SentimentIntensityAnalyzer()
		reload(sys)
		sys.setdefaultencoding("utf-8")
		m = Text(nltk.corpus.gutenberg.words('userReviews.txt'))

		specs = ['product','battery','price','weight','touch','heat','slow','performance','ram']

		for res in specs:

			fileconcord = open(res+'.txt', 'w')
			tmpout = sys.stdout
			sys.stdout = fileconcord
			m.concordance(res, 200, sys.maxint)
			fileconcord.close()
			sys.stdout = tmpout

		file = open('sentimentwords.txt')

		dictionary = collections.defaultdict(lambda : 0)
		for token in file:
			dictionary[token[:-1]] = 1
		#print dictionary
		#print sentimentfile
		pic = []
		for res in specs :
			fileconcord  = open(res+'.txt','r')
			sent_pol = []
			for line in fileconcord:
				line = line.split()
				line_new=[]
				#print line
				for tok in line:
					if dictionary[tok] :
						#print tok
						line_new.append(tok)
				line =' '.join(line_new)
				if res=='heat':
					print line
				sent_pol.append( sid.polarity_scores(line)['compound'])
			print res
			pic.append(res)
			xx = sum(1 for i in sent_pol if i>0)*1.0/len(sent_pol)
			print xx
			pic.append(xx)
			#print sum(i for i in sent_pol )/len(sent_pol)
			#print sent_pol
			print
		
		return pic