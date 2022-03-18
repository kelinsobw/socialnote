from django.contrib import admin
from django.urls import path
from . import views
from .views import index, add_database

urlpatterns = [
    path('', index),
    path("add_basadate", add_database),
]
