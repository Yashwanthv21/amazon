from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import Amazon_Analyse

import json
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data, comments= q.analyse_class()

		#for testing display
		dictionary = {
				'battery' : ['bad battery','good battery','worst battery'],
				'camera' : ['badcamera','goodcamera','worstcamera'],
				'look' : ['bad','good','worst'],
				'design' : ['bad','good','worst']
		}
		f = open("product-title.txt")
		title = ""
		for line in f:
			title += line.strip()

		return  render(request, 'result.html', {'data': data, 'comments': json.dumps(comments),'title':title})

def analyse_data_list_all(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data = q.analyse_class()
		return  render(request, 'index.html', {'data': data})

