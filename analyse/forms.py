from django import forms

class ScrapeForm(forms.Form):
    spec = forms.CharField(label='specification', max_length=1000)

