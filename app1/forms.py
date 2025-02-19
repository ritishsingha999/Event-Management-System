from django import forms
from app1.models import Category




class event_form(forms.Form):
     name = forms.CharField(max_length=100,label="Event Name")
     description = forms.CharField(widget=forms.Textarea, label="Event Description")
     date = forms.DateField(label="Event Date", widget=forms.DateInput(attrs={'type': 'date'}))
     time =forms.DateField(widget=forms.TimeInput(attrs={'type': 'time'}))
     location =forms.CharField(max_length=100, label="Event Location")
     category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Event Category") 
