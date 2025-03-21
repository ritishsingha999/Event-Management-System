# from django.shortcuts import render, redirect
# from django.forms import ModelForm
# from django.forms import widgets
# from app1.mixins import StyledFormMixin
from django import forms
from app1.models import Category, Event, Participant


class EventSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    date = forms.DateField(label='Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    participant = forms.ModelChoiceField(queryset=Participant.objects.all(), required=False)
    location = forms.CharField(label='Location', max_length=100, required=False, initial='Chattogram')
    status = forms.ChoiceField(choices=Event.EVENT_STATUS_CHOICES, required=False)
    

class StyledFormMixin:
    """Mixin for styling form widgets"""
    default_classes = "input-class border-2 border-teal-100 w-full shadow-sm focus:border-teal-50 focus:bg-teal-50 rounded-lg"
    
    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter new event {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'date'
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'time'
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'datetime-local'
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })

        
class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category', 'status', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-100 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg', 'placeholder': ' Enter event name...'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg', 'placeholder': ' Event Description', 'rows': 4}),
            'date': forms.DateInput(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg', 'placeholder': ' Event Location'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg'}),
            'status': forms.Select(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border-2 border-teal-400 shadow-sm focus:ring-2 focus:ring-blue-500 rounded-lg'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

