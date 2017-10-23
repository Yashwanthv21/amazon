from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Amazon_Analyse
from .forms import ScrapeForm
import json
import re
# Create your views here.

def analyse_data(request):
	if request.method == 'GET':
		print "im in get function"
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
		form = ScrapeForm()
		specs_list = []
		p = []
		f = open('specs.txt')
		for line in f:
			print line
			p.append(re.findall(r'"(.*?)"',line))
		#print p
		for i in xrange(0,len(p),2):
			specs_list.append((p[i][0],p[i+1][0]))
		print specs_list
		return  render(request, 'result.html', {'data': data, 'comments': json.dumps(comments),'title':title, 'image':base64,'form':form,'specs_list':specs_list})
	

def analyse_data_list_all(request):
	if request.method == 'GET':
		q = Amazon_Analyse()
		data, comments = q.analyse_class()
		return  render(request, 'index.html', {'data': data})

def analyse_newspec(request):
	if request.method == 'POST' and request.is_ajax:
		print "im in post function"
		form = ScrapeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #name_obj = Amazon_Url.objects.create(url=form.cleaned_data['url'] )
            spec = form.cleaned_data['spec']
            print spec
            print 'hello'
            qq = Amazon_Analyse()
            value, comments = qq.Amazon_spec(spec)
            #print 'Url is', url
            print 'value is' ,value
            print comments
            data = json.dumps({
            	'heading': spec, 
            	'value': value,
            	'comments_spec':comments,
            	})
            return JsonResponse(data,safe = False)
            print 'not sent'