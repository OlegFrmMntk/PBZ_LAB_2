from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('pokemon', index),
    path('owners', owners, name='owner'),
    path('exhibitions', exhibitions, name='exhibition'),
    path('exhibition_halls', exhibition_halls, name='exhibition_hall'),
    path('artists', artists, name='artist'),
    path('artworks', artworks, name='artwork'),
    path('exhibitions_artists', exhibitions_and_artists, name='exhibitions_artists'),
    path('exhibition_hall_in_city', exhibition_hall_in_city, name='exhibition_hall_in_city'),
    path('now_exhibitions', now_exhibitions, name='now_exhibitions')
]
