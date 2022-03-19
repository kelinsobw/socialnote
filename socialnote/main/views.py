import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from main.forms import  AddDatabase

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "main/register.html")


def add_database(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddDatabase(request.POST, request.FILES)
            if form.is_valid():
                info_base = form.cleaned_data
                print(info_base)
                return HttpResponse("You don't authenticated!")
        else:
            form = AddDatabase()
        return render(request, "main/add_base.html", {"form": form})
    return HttpResponse("You don't authenticated!")
