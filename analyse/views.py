from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import ScrapeForm

from .models import Amazon_Analyse
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data= q.analyse_class()
		form = ScrapeForm()
		return  render(request, 'result.html', {'data': data,'form':form})

def analyse_data_list_all(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data = q.analyse_class()
		form = ScrapeForm()
		return  render(request, 'index.html', {'data': data})

