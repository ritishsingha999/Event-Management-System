from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.db.models import Q, Count, Max, Min, Avg, Sum
from django.contrib import messages
from rest_framework import generics
from django.contrib.postgres.search import SearchVector
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from .models import Participant, Event, Category  
from app1.models import Event, Participant, Category
from app1.forms import EventSearchForm, EventModelForm

# from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
# from users.views import is_admin
# from django.utils.decorators import method_decorator
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.views.generic.base import ContextMixin
# from django.views.generic import ListView, DetailView, UpdateView







# # Create your views here.










    
def search_events(request):
    form = EventSearchForm(request.GET or None)
    results = []
    query = request.GET.get('q', '')  # Get search query
    # events = Event.objects.all()
    events = Event.objects.annotate(
        search=SearchVector('name', 'category', 'participants__name')
    ).filter(search=query) if query else Event.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        date = form.cleaned_data.get('date')
        category = form.cleaned_data.get('category')
        location = form.cleaned_data.get('location')



    if query or date:
            q_objects = Q()

            if query:
                q_objects |= Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(participant__name__icontains=query)
            
            if date:
                q_objects &= Q(date__date=date)
                
            if query:
                q_objects |= Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(participant__name__icontains=query)
            
            if category:
                q_objects &= Q(category=category)
            
            if location:
                q_objects &= Q(location__icontains=location)
            
            if q_objects:
                results = Event.objects.filter(q_objects).distinct()

            results = Event.objects.filter(q_objects).distinct()
            
    if query:
        events = events.filter(
            Q(name__icontains=query) |  # Search by event name
            Q(date__icontains=query) |  # Search by date
            Q(category__icontains=query) |  # Search by category
            Q(participants__name__icontains=query)  # Search by participant name
        ).distinct()

    
    
    return render(request, 'Events/Search_Events.html', {'form': form, 'results': results, 'events': events})



# from app1.serializers import EventSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    # serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'date', 'category', 'participants__name']



def finance(request):
    return render(request, 'Dashboard/OrganizerDashboard/finance.html')

def event_categorys(request):
    categorys = Category.objects.prefetch_related()
    return render(request, 'Categorys\categorys.html', {'categorys': categorys})

def admin_panel(request):
    type = request.GET.get('type', 'all')
    
    counts = Event.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='completed')),
        ongoing=Count('id', filter=Q(status='ongoing')),
        pending=Count('id', filter=Q(status='upcoming')),
    )
    
    base_query = Event.objects.all()
    if type == 'completed':
        events = base_query.filter(status='completed')
    elif type == 'ongoing':
        events = base_query.filter(status='ongoing')
    elif type == 'upcoming':
        events = base_query.filter(status='upcoming')
    elif type == 'all':
        events = base_query.all()
        
    all_events = Event.objects.all().select_related()
    total_events = all_events.count()
    upcoming_events = all_events.filter(status='upcoming').count()
    ongoing_events = all_events.filter(status='ongoing').count()
    completed_events = all_events.filter(status='completed').count()
    all_participants = Participant.objects.all().prefetch_related()
    total_participants = all_participants.count()
    locations = Event.objects.values_list('location', flat=True).distinct()
    total_categories = Category.objects.all().select_related().count()  
    future_date = datetime.now() + timedelta(days=70, hours=19, minutes=14, seconds=46)
    context = {
        'participants': all_participants,
        'total_participants': total_participants,
        'total_events': total_events,
        'all_events': all_events,  
        'upcoming_events': upcoming_events,
        'ongoing_events': ongoing_events,
        'completed_events': completed_events,
        'total_categories': total_categories,  
        'future_date': future_date,
        'locations': locations,
        'counts': counts,
        'events': events
    }
    return render(request, 'Dashboard/OrganizerDashboard/Admin_Panel.html', context)



def dashboard01(request):
    search_query = request.GET.get('search', '').strip()  
    # print(type)


    counts = Event.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='completed')),
        ongoing=Count('id', filter=Q(status='ongoing')),
        pending=Count('id', filter=Q(status='upcoming')),
    )


    type = request.GET.get('type', 'all')
# # Retriving Event data

    # base_query = Event.objects.select_related('category').prefetch_related('participants')
    base_query = Event.objects.all()
    if type == 'completed':
        events = base_query.filter(status='completed')
    elif type == 'ongoing':
        events = base_query.filter(status='ongoing')
    elif type == 'upcoming':
        events = base_query.filter(status='upcoming')
    elif type == 'all':
        events = base_query.all()
    
    
    
    
    
    if search_query:
        all_events = Event.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        ).select_related()
    else:
        all_events = Event.objects.all().select_related()

    total_events = all_events.count()
    upcoming_events = all_events.filter(status='upcoming').count()
    ongoing_events = all_events.filter(status='ongoing').count()
    completed_events = all_events.filter(status='completed').count()
    all_participants = Participant.objects.all().prefetch_related()
    total_participants = all_participants.count()
    locations = Event.objects.values_list('location', flat=True).distinct()
    total_categories = Category.objects.all().select_related().count()  
    future_date = datetime.now() + timedelta(days=70, hours=19, minutes=14, seconds=46)

    context = {
        'participants': all_participants,
        'total_participants': total_participants,
        'total_events': total_events,
        'all_events': all_events,  
        'upcoming_events': upcoming_events,
        'ongoing_events': ongoing_events,
        'completed_events': completed_events,
        'total_categories': total_categories,  
        'future_date': future_date,
        'locations': locations,
        'search_query': search_query,
        'counts': counts,
        'events': events
    }

    return render(request, 'Dashboard/OrganizerDashboard/Dashboard.html', context)
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
    # events = Event.objects.all()  # DB
    from app1.forms import EventModelForm  # Ensure this import is at the top of the file
    form = EventModelForm()  # for GET by default
    if request.method == "POST":
        form = EventModelForm(request.POST)
        if form.is_valid():
            
            ''' For Django Model Form DATA '''
            form.save()
            return render(request,"Dashboard/OrganizerDashboard/Form1.html",{"form":form,"message":"Event Added Successfully."})

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
            # return HttpResponse("Event Added Successfully.")
            
            # print(form.cleaned_data) 
    context={"form":form}
    return render(request,"Dashboard/OrganizerDashboard/Form1.html",context)
    
def form2(request):
    return render(request, 'Dashboard/OrganizerDashboard/Form2.html')


def view_event(request):
    # Retrieving Data from the Database
     
    # # retrive a spacific event
    # event3=Event.objects.get(id=3)
    # return render(request, 'Events/ViewEvent.html', {'events': events, 'event3': event3})
    
    # # fetch first event
    # first_event = Event.objects.first()
    # return render(request, 'Events/ViewEvent.html', {'events': events,'first_event':first_event})
    
    # # Filtering Data
    # events=Event.objects.filter('Category=Tech Conference')
    # return render(request, 'Events/ViewEvent.html', {'events': events})
    
    # events=Event.objects.filter(date=date.today())
    # return render(request, 'Events/ViewEvent.html', {'events': events})
    
    # # exclude use
    # events=Event.objects.exclude(date=date.today())
    # return render(request, 'Events/ViewEvent.html', {'events': events})
    
    events = Event.objects.select_related() #more optimized then all()
    # events = Event.objects.all()
    return render(request, 'Events/ViewEvent.html', {'events': events})

def participants_view(request):
    # participants = Participant.objects.all()
    # participants = Participant.objects.prefetch_related()
    participants = Participant.objects.prefetch_related()
    total_participants = participants.count()
    context={
           'participants': participants,
           'total_participants': total_participants
    }
    # print(participants)
    return render(request, 'Participants/ALL_participants.html',context)

# def form1(request):
#     form = event_form(initial={"event_type_or_category": "ceremonial_event", "event_id": 1})  # for GET by default
#     if request.method == "POST":
#         form = event_form(request.POST)
#         if form.is_valid():
#             # Process the form data
#             pass
#     context = {"form": form}
#     return render(request, 'Dashboard/OrganizerDashboard/Form1.html', context)




# def create_event(request):
#     # if request.method == "POST":
#     #     form = EventForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('event_list')
#     # else:
#     #     form = EventForm()
#     eventmodelform =event_model_form()
#     # eventdetailmodelform=event_detail_model_form()
#     if request.method == "POST":
#         eventmodelform =event_model_form(request.POST)
#         # eventdetailmodelform=event_detail_model_form(request.POST)
        
#         if eventmodelform.is_valid():
#             events=eventmodelform.save()
#             # eventdetails=eventdetailmodelform.save(commit=False)
#             # eventdetails.description=events
#             # eventdetails.save()
#     messages.success(request, "Event Created Successfully")
#     return render(request, 'Events/Create_Event.html', {'events':events, "messages": 'Event Created Successfully'})
#     # return redirect('create_event')
# def update_event(request,id):
#     event = Event.objects.get(id=id)
#     # if request.method == "POST":
#     #     form = EventForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('event_list')
#     # else:
#     #     form = EventForm()
#     eventmodelform =event_model_form()
#     eventdetailmodelform=event_detail_model_form()
#     if request.method == "POST":
#         eventmodelform =event_model_form(request.POST, instance=event)
#         eventdetailmodelform=event_detail_model_form(request.POST)
        
#         if eventmodelform.is_valid() and eventdetailmodelform.is_valid():
#             events=eventmodelform.save()
#             eventdetails=eventdetailmodelform.save(commit=False)
#             eventdetails.description=events
#             eventdetails.save()
#     messages.success(request, "Event Created Successfully")
#     return render(request, 'Events/Create_Event.html', {'eventmodelform': eventmodelform, 'eventdetailmodelform': eventdetailmodelform, "messages": 'Event Created Successfully'})







def create_event(request):
    eventmodelform = EventModelForm()

    if request.method == "POST":
        eventmodelform = EventModelForm(request.POST, request.FILES)
        if eventmodelform.is_valid():
            eventmodelform.save()
            messages.success(request, "Event Created Successfully")
            return redirect('event_list')  

    return render(request, 'events/create_event.html', {'eventmodelform': eventmodelform})

def update_event(request, id):
    # event=Event.objects.get(id=id)
    event = get_object_or_404(Event, id=id)
    eventmodelform = EventModelForm(instance=event)

    if request.method == "POST":
        eventmodelform = EventModelForm(request.POST, request.FILES, instance=event)
        if eventmodelform.is_valid():
            eventmodelform.save()
            messages.success(request, "Event Updated Successfully")
            return redirect('create_event')  

    return render(request, 'events/create_event.html', {'eventmodelform': eventmodelform})

def delete_event(request, id):
    # event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event=Event.objects.get(id=id)
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('dashboard')
    else:
        messages.error(request, "Error Deleting Event [Something went wrong]")
        return redirect('dashboard')
        # return render(request, 'events/delete_event.html', {'event': event})

def ds2(request):
    return render(request, 'Dashboard/OrganizerDashboard/ds2.html')










# def create_event(request):
#     if request.method == 'POST':
#         # ... your form handling logic ...
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('success_page')) # Redirect to a success page
#     else:
#         form = event_modelform()
#     return render(request, "create_event.html", {'form': form})

def search_events(request):
    return render(request, 'Events/Search_Events.html')
        
def testing(request):
    return render(request, 'Dashboard/OrganizerDashboard/testing.html')
