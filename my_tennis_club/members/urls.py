from django.urls import path
from .views import members,details,main

urlpatterns = [
    path('',main, name="home"),
    path('members/', members, name='members'),
    path('members/details/<int:id>',details,name="details")
]