from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import Amazon_Analyse

import json
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data, comments= q.analyse_class()

		f = open("product-title.txt")
		title = ""
		for line in f:
			title += line.strip()

		#getting image data
		imageFile = open("imageData.txt")
		base64 = imageFile.readline()
		base64 = base64[3:]
		return  render(request, 'result.html', {'data': data, 'comments': json.dumps(comments),'title':title, 'image':base64})

def analyse_data_list_all(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data, comments = q.analyse_class()
		return  render(request, 'index.html', {'data': data})

