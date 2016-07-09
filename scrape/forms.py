from django import forms

class ScrapeForm(forms.Form):
    url = forms.CharField(label='Url of product', max_length=1000)

