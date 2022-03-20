import datetime
import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.forms import  AddDatabase
from main.models import Databases, Privates
from main.postgres_def import create_table, get_the_date

logger = logging.getLogger(__name__)


def my_list(request):
    bases = Databases.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "main/list.html", {"bases": bases})


def index(request):
    bases = Databases.objects.order_by("-created_at")
    return render(request, "main/list.html", {"bases": bases})


def add_database(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddDatabase(request.POST, request.FILES)
            if form.is_valid():
                info_base = form.cleaned_data
                create_table(info_base)
                my_base = Databases.objects.create(
                    author=request.user,
                    db_name=info_base.get("table_name"),
                    db_description=info_base.get("table_description"),
                    created_at=datetime.datetime.now()
                )

                Privates.objects.create(
                    base=my_base,
                    privates=info_base.get("table_privates")
                )
            return HttpResponse("You don't authenticated!")
        else:
            form = AddDatabase()
        return render(request, "main/add_base.html", {"form": form})
    return HttpResponse("You don't authenticated!")


def table_view(request, db_name):
    bases =
    bases = get_the_date(db_name)
    return render(request, "main/table_view.html", {"bases": bases})
