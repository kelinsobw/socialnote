"""socialnote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from main.views import add_database, table_view, add_data, del_data
from socialnote.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    path("register/", register, name="register"),
    path("add_basadate/", add_database),
    path("add_basadate/", add_database),
    path("table_view/<str:db_name>", table_view, name="table_view"),
    path("add_data/<str:db_name>", add_data, name="add_data"),
    path("table_view/del_data/<str:db_name>", del_data, name="del_data")
]
