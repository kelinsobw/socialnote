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
from django.urls import path

from main.views import add_database, table_view, add_data, del_data, my_list, error_access, index
from socialnote.views import register, register_2, login_user, login_user_reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("home/", index),
    path("my_list/", my_list, name="my_list"),
    path("register/", register, name="register"),
    path("register_2/", register_2, name="register_2"),
    path("add_basadate/", add_database),
    path("table_view/<str:db_name>", table_view, name="table_view"),
    path("add_data/<str:db_name>", add_data, name="add_data"),
    path("del_data/<str:db_name>/<str:id>", del_data, name="del_data"),
    path('login/', login_user),
    path('login_user_reg/', login_user_reg, name='login_user_reg'),
    path('error/', error_access),
]

