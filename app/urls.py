from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [

    path('pokemon', index),
    path('owners', owners, name='own'),
]