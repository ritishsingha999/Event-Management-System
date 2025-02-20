from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Participant, Event, Category  
from app1.forms import event_modelform
from app1.models import Event, Participant, Category
from .forms import event_modelform
# # Create your views here.

def dashboard(request):
    # today = timezone.now().date()
    # stats = {
    #     'total_participants': Participant.objects.count(),
    #     'total_events': Event.objects.count(),
    #     'upcoming_events': Event.objects.filter(date__gte=today).count(),
    #     'past_events': Event.objects.filter(date__lt=today).count(),
    # }
    
    # todays_events = Event.objects.filter(date=today).select_related('category')
    
    # view_type = request.GET.get('view', 'today')
    # if view_type == 'all':
    #     events = Event.objects.all()
    # elif view_type == 'upcoming':
    #     events = Event.objects.filter(date__gte=today)
    # elif view_type == 'past':
    #     events = Event.objects.filter(date__lt=today)
    # else:
    #     events = todays_events
    
    # context = {
    #     'stats': stats,
    #     'todays_events': todays_events,
    #     'events': events,
    #     'view_type': view_type,
    # }
    # return render(request, 'events/dashboard.html', context)
    return render(request, 'Dashboard/OrganizerDashboard/Organizer_Dashboard_01.html')

# def create_event(request):
#     # if request.method == "POST":
#     #     form = EventForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('event_list')
#     # else:
#     #     form = EventForm()
#     return render(request, 'events/create_event.html', {'form': form})

# def event_list(request):
#     # events = Event.objects.all()
#     return render(request, 'events/event_list.html', {'events': events})

# def update_event(request, pk):
#     # event = get_object_or_404(Event, pk=pk)
#     # if request.method == "POST":
#     #     form = EventForm(request.POST, instance=event)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('event_list')
#     # else:
#     #     form = EventForm(instance=event)
#     return render(request, 'events/update_event.html', {'form': form})

# def delete_event(request, pk):
#     # event = get_object_or_404(Event, pk=pk)
#     # if request.method == "POST":
#     #     event.delete()
#     #     return redirect('event_list')
#     return render(request, 'events/delete_event.html', {'event': event})


# def form1(request):
#     events=Event.objects.all() #DB
#     form=event_form(events=events) #for GET by defult 
#     # form=event_form(Ct1={"event_type_or_catagory":"ceremonial_event", "event_id":1}) #for GET by defult 
#     if request.method == "POST":
#         form = event_form(request.POST, events=events)
#         if form.is_valid():
#             data=form.cleaned_data
#             name=data.get('name')
#             description=data.get('description')
#             date=data.get('date')
#             time=data.get('time')
#             location=data.get('location')
#             category=data.get('category')
            
#             event=Event.objects.create(name=name, description=description, date=date, time=time, location=location)
#             event.objects.add()
            
            
            
#             # Assign catagoty to event
#             for ct_id in category:
#                 ct = Category.objects.get(id=ct_id)
#                 event.category.add(ct)
#             return HttpResponse("Event Added Successfully.")
            
#             # print(form.cleaned_data) 
#     context={"form":form}
#     return render(request,"Dashboard/OrganizerDashboard/Form1.html",context)
#     # return render(request, 'Dashboard/OrganizerDashboard/Form1.html')

def form1(request):
    events = Event.objects.all()  # DB
    form = event_modelform()  # for GET by default
    if request.method == "POST":
        form = event_modelform(request.POST)
        if form.is_valid():
            
            ''' For Django Model Form DATA '''
            form.save()
            
            ''' For Django Form DATA '''
            # data=form.cleaned_data
            # name=data.get('name')
            # description=data.get('description')
            # date=data.get('date')
            # time=data.get('time')
            # location=data.get('location')
            # category=data.get('category')
            
            # event=Event.objects.create(name=name, description=description, date=date, time=time, location=location)
            # event.objects.add()
            
            
            
            # # Assign catagoty to event
            # for ct_id in category:
            #     ct = Category.objects.get(id=ct_id)
            #     event.category.add(ct)
            return HttpResponse("Event Added Successfully.")
            
            # print(form.cleaned_data) 
    context={"form":form}
    return render(request,"Dashboard/OrganizerDashboard/Form1.html",context)
    



# def form1(request):
#     form = event_form(initial={"event_type_or_category": "ceremonial_event", "event_id": 1})  # for GET by default
#     if request.method == "POST":
#         form = event_form(request.POST)
#         if form.is_valid():
#             # Process the form data
#             pass
#     context = {"form": form}
#     return render(request, 'Dashboard/OrganizerDashboard/Form1.html', context)