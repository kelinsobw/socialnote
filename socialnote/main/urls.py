from django.contrib import admin
from django.urls import path
from . import views
from .views import index, add_database, my_list, table_view

urlpatterns = [
    path('', index),
    path('my_list/', my_list),
    path("add_basadate/", add_database),
    path("table_view/", table_view),
]
