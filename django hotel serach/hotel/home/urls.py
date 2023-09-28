from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path,include
urlpatterns = [
    path('api/get-hotels/',get_hotel),
]
