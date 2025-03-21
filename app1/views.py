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



    
def search_events(request):
    form = EventSearchForm(request.GET or None)
    results = []
    query = request.GET.get('q', '')  
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


    counts = Event.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='completed')),
        ongoing=Count('id', filter=Q(status='ongoing')),
        pending=Count('id', filter=Q(status='upcoming')),
    )


    type = request.GET.get('type', 'all')

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
    return render(request, 'Dashboard/OrganizerDashboard/Organizer_Dashboard_01.html')


def form1(request):
    from app1.forms import EventModelForm  
    form = EventModelForm()  
    if request.method == "POST":
        form = EventModelForm(request.POST)
        if form.is_valid():
            
            ''' For Django Model Form DATA '''
            form.save()
            return render(request,"Dashboard/OrganizerDashboard/Form1.html",{"form":form,"message":"Event Added Successfully."})
    context={"form":form}
    return render(request,"Dashboard/OrganizerDashboard/Form1.html",context)
    
def form2(request):
    return render(request, 'Dashboard/OrganizerDashboard/Form2.html')


def view_event(request):
    events = Event.objects.select_related() #more optimized then all()
    return render(request, 'Events/ViewEvent.html', {'events': events})

def participants_view(request):
    participants = Participant.objects.prefetch_related()
    total_participants = participants.count()
    context={
           'participants': participants,
           'total_participants': total_participants
    }
    return render(request, 'Participants/ALL_participants.html',context)





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


def search_events(request):
    return render(request, 'Events/Search_Events.html')
        
def testing(request):
    return render(request, 'Dashboard/OrganizerDashboard/testing.html')
