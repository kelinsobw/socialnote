import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.forms import AddDatabase

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "main/register.html")


def add_database(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddDatabase(request.POST, request.FILES)
            if form.is_valid():
                print("0000000000000000000000000000000000000000")
                return redirect("main/home")
        else:
            form = AddDatabase()
        return render(request, "main/home.html", {"form": form})
    return HttpResponse("You don't authenticated!")