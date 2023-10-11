from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 
from . import views;
from contacts import views as contact_view
from services import views as mainservices


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path('accounts/', include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('about/', views.about, name='about'),
    path('all_service/', mainservices.mainservices, name='all_services'),
    path('festive/', mainservices.festive_service, name='festival_puja' ),
    path('festive/details/<int:id>', mainservices.details, name='details'),
    path('contact/',contact_view.contact_view,name='contact'),
    path('havan/', views.havan, name='havan' ),
    path('pandit/', views.pandit, name='pandit' ),
    path('termandservice/', views.termandservice, name='termandservice' ),
   
]
