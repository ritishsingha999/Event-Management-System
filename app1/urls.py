
from django.urls import path
from .views import dashboard
from app1.views import dashboard, form2, view_event, participants_view, dashboard01, admin_panel, event_categorys, finance, create_event, update_event, search_events, testing, ds2, delete_event


urlpatterns = [
    path('Organizer_Dashboard_01/', dashboard, name='Organizer_Dashboard_01'),
    path('form_2/',form2,name='form_2'),
    path('viewevents/',view_event, name='viewevents'),
    path('ALL_participants/',participants_view, name='ALL_participants'),
    path('dashboard/', dashboard01, name='dashboard'),
    path('adminpanel/',admin_panel, name='adminpanel'),
    path('event_categorys/',event_categorys, name='event_categorys'),
    path('finance/',finance, name='finance'),
    path('search_events/',search_events, name='search_events'),
    path('testing',testing, name='testing'),
    path('create_event/',create_event, name='create_event'),
    path('update_event/<int:id>/', update_event, name='update_event'),
    path('delete_event/<int:id>/', delete_event, name='delete_event'),
    path('ds2/',ds2, name='ds2')    
] 
