from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('service/',views.service, name='service'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog, name='blog'),
]
