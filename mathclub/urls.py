from django.urls import path
from . import views

app_name = "mathclub"

urlpatterns = [
    path('', views.index, name="index"),
    path('team/', views.team, name="team"),
    path('about/', views.about, name="about"),
    path('events/', views.events, name="events"),
    path('contact/', views.contact, name="contact"),
    path('study', views.study, name="study"),
]