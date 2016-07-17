from django import forms

class ScrapeForm(forms.Form):
    spec = forms.CharField(label='', max_length=1000)

