
from django.urls import path
from .views import dashboard
from app1.views import dashboard, form1

urlpatterns = [
    # path("show/",show, name='show')
    path('Organizer_Dashboard_01/', dashboard, name='Organizer_Dashboard_01'),
    # path('EMS_01/', dashboard, name='EMS_01'),
    path('form_1/',form1,name='form_1')
    
    
] 
