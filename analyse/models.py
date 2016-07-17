from __future__ import unicode_literals
import os 
from django.db import models
import math
import nltk
import nltk.corpus
from nltk.text import Text
import sys
import collections
import io
import os.path
from nltk.tokenize import sent_tokenize

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Create your models here.

class Amazon_Analyse(models.Model):
	def analyse_class(self):
		
		#start = timeit.default_timer()
		sid = SentimentIntensityAnalyzer()
		reload(sys)
		sys.setdefaultencoding("utf-8")
		path = os.getcwd()
		m = Text(nltk.corpus.gutenberg.words(path + '/userReviews.txt'))

		specs = ['camera','performance','battery','look','feel','money','sound','network','storage','software']

		save_path = path + '/analyse/data/'
				 
		for spec in specs:

			completeFileName = os.path.join(save_path, spec+".txt")
			specFile = open(completeFileName, 'w')
			tmpout = sys.stdout
			sys.stdout = specFile
			m.concordance(spec, 200, sys.maxint)
			specFile.close()
			sys.stdout = tmpout		
		
		file = open('sentimentwords.txt')

		dictionary = collections.defaultdict(lambda : 0)
		comments =  collections.defaultdict(lambda : [])
		for token in file:
			dictionary[token[:-1]] = 1
		# print dictionary
		# print sentimentfile
		data = []
		for spec in specs :
			completeFileName = os.path.join(save_path, spec+".txt")
			specFile  = open(completeFileName, 'r')
			sent_pol = []
			for line in specFile:
				line1 = line[:]
				line = line.split()
				# print line
				line_new=[]

				for tok in line:
					if dictionary[tok] :
						# print tok
						line_new.append(tok)
				line =' '.join(line_new)
				sent_pol.append( sid.polarity_scores(line)['compound'])
				comments[spec].append((sid.polarity_scores(line)['compound'],line1))
			comments[spec].sort()
			print spec
			sentiment_value = sum(1 for i in sent_pol if i>0)*1.0/len(sent_pol)
			sentiment_value = round(sentiment_value,2) * 10
			print sentiment_value
			data.append((spec,sentiment_value)) 
			#print sum(i for i in sent_pol )/len(sent_pol)
			#print sent_pol
			print
		
		return data,comments


	def Amazon_spec(self,tokenn):

		
		sid = SentimentIntensityAnalyzer()
		reload(sys)
		sys.setdefaultencoding("utf-8")
		path = os.getcwd()
		m = Text(nltk.corpus.gutenberg.words(path + '/userReviews.txt'))

		specs = [tokenn]

		save_path = path + '/analyse/data/'
				 
		for spec in specs:

			completeFileName = os.path.join(save_path, spec+".txt")
			specFile = open(completeFileName, 'w')
			tmpout = sys.stdout
			sys.stdout = specFile
			m.concordance(spec, 200, sys.maxint)
			specFile.close()
			sys.stdout = tmpout		
		
		file = open('sentimentwords.txt')

		dictionary = collections.defaultdict(lambda : 0)
		comments =  collections.defaultdict(lambda : [])
		for token in file:
			dictionary[token[:-1]] = 1
		# print dictionary
		# print sentimentfile
		data = []
		for spec in specs :
			completeFileName = os.path.join(save_path, spec+".txt")
			specFile  = open(completeFileName, 'r')
			sent_pol = []
			for line in specFile:
				line1 = line[:]
				line = line.split()
				# print line
				line_new=[]

				for tok in line:
					if dictionary[tok] :
						# print tok
						line_new.append(tok)
				line =' '.join(line_new)
				sent_pol.append( sid.polarity_scores(line)['compound'])
				comments[spec].append((sid.polarity_scores(line)['compound'],line1))
			comments[spec].sort()
			print spec
			sentiment_value = sum(1 for i in sent_pol if i>0)*1.0/len(sent_pol)
			sentiment_value = round(sentiment_value,2) * 10
			print sentiment_value
			data.append((spec,sentiment_value)) 
			#print sum(i for i in sent_pol )/len(sent_pol)
			#print sent_pol
			print
		
		return data[0][1],comments
