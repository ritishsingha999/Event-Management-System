# from django.contrib import admin
# from django.urls import path
# from app2.views import home, contact

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("home/",home),
#     # path("about/",about),
#     path("contact/",contact),
#     # path("events/", events),
#     # path("event/<int:event_id>/", event_detail),
#     # path("event/<int:event_id>/register/", register_event),
# ]


from django.contrib import admin
from django.urls import path
# from app2 import views
from app1 import views
from django.urls import include 
from  debug_toolbar.toolbar import debug_toolbar_urls
# from django.urls import include as includes 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls'))
    # path('home/', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('app2/',include('app2.urls')),
    
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)