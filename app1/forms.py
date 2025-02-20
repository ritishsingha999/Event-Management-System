from django import forms
from app1.models import Category, Event, Participant


          
#  Django Model Form 
class event_modelform(forms.ModelForm):
     class Meta:
          model = Event
          # fields = '__all__'
          # fields = ['name', 'description']
          # exclude = ['location', 'date', 'time']
          fields = ['name', 'description', 'date', 'time', 'location', 'category']
          widgets = {
            'name': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Event Name'}),
            'description': forms.Textarea(attrs={'class': 'textarea-class', 'placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'class': 'input-class', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'input-class', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Event Location'}),
            'category': forms.Select(attrs={'class': 'select-class'}),
        }
          
          

# Django Form (Basic one)
# class event_form(forms.Form):
#      name = forms.CharField(max_length=100,label="Event Name")
#      description = forms.CharField(widget=forms.Textarea, label="Event Description")
#      # date = forms.DateField(label="Event Date", widget=forms.DateInput(attrs={'type': 'date'}))
#      date = forms.DateField(label="Event Date", widget=forms.SelectDateWidget)
#      time =forms.DateField(widget=forms.TimeInput(attrs={'type': 'time'}))
#      location =forms.CharField(max_length=100, label="Event Location")
#      # category = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple queryset=Category.objects.all(), label="Event Category") 
#      category = forms.ModelChoiceField( queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple, label="Event Category", choices=[]) 
     
#      def __init__(self,*args,**kwargs):
#           # print(args, kwargs)
#           events=kwargs.pop("Ct",[])
#           print(events)
#           super().__init__(*args,**kwargs)
#           # print(self.fields)
#           self.fields["event"].choices=[(event.name,event.id) for event in events]