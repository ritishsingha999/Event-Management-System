from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Participant, Event  
from app1.forms import event_form

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


def form1(request):
    form=event_form()
    context={'form':form}
    return render(request,'Dashboard/OrganizerDashboard/Form1.html',context)
    # return render(request, 'Dashboard/OrganizerDashboard/Form1.html')

