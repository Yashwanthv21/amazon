from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import Amazon_Analyse
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data= q.analyse_class()
		return  render(request, 'result.html', {'data': data})

def analyse_data_list_all(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data = q.analyse_class()
		return  render(request, 'index.html', {'data': data})

