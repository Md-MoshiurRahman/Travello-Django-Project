from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.index, name='index'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('news',views.news, name='news'),
    path('contact',views.contact, name='contact'),
    path('destinations',views.destinations, name='destinations')
    ]