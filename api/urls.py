
from django.urls import path, include
from rest_framework import routers
from .views import homepageview



urlpatterns = [
    path("", homepageview),
]