from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ScrapeForm
#from .models import Name

def get_data(request):
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScrapeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name_obj = Name.objects.create(your_name=form.cleaned_data['your_name'] )
            print 'your name is', name_obj.your_name
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
    	form = ScrapeForm()

    return render(request, 'data.html', {'form': form})