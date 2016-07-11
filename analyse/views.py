from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import ScrapeForm

from .models import Amazon_Analyse
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		picc = q.analyse_class()
		form = ScrapeForm()
		return  render(request, 'tes.html', {'picc': picc,'form':form})

