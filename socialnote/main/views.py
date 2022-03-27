import datetime
import logging

from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.forms import AddDatabase
from main.models import Databases, Privates
from main.postgres_def import create_table, get_the_date, view_colums_table, view_column_type, add_an_enrty, \
    delete_record

logger = logging.getLogger(__name__)


def my_list(request):
    try:
        bases = Databases.objects.filter(author=request.user).order_by("-created_at")
    except:
        return HttpResponse("No data available")
    return render(request, "main/my_list.html", {"bases": bases})



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
            return redirect(f"/add_data/{info_base.get('table_name')}")
        else:
            form = AddDatabase()
        return render(request, "main/add_base.html", {"form": form})
    return HttpResponse("You don't authenticated!")


def table_view(request, db_name):

    bases_res = []
    name = []
    name.append(db_name)
    bases = get_the_date(db_name)
    bases_temp_1 = bases[1]
    bases_temp_1 = bases_temp_1[0]
    for i in range(0, len(bases_temp_1)-1):
        name.append(" ")
    bases_res.append(name)
    bases_res.append(list(bases[0]))
    for element in bases_temp_1:
        bases_res.append(list(element))
    bases = bases_res
    return render(request, "main/table_view.html", {"bases": bases})


def add_data(request, db_name):
    class Forms_add(forms.Form):
        types = view_column_type(db_name)
        try: base_1 = forms.CharField(label=types[1])
        except: pass
        try: base_2 = forms.CharField(label=types[2])
        except: pass
        try: base_3 = forms.CharField(label=types[3])
        except: pass
        try: base_4 = forms.CharField(label=types[4])
        except: pass
        try: base_5 = forms.CharField(label=types[5])
        except: pass
        try: base_6 = forms.CharField(label=types[6])
        except: pass
        try: base_7 = forms.CharField(label=types[7])
        except: pass

    if request.user.is_authenticated:
        if request.method == "POST":
            form = Forms_add(request.POST, request.FILES)
            if form.is_valid():
                info_base = form.cleaned_data
                add_an_enrty(db_name, info_base)
            return redirect(f"/table_view/{db_name}")
        else:
            form = Forms_add()
        return render(request, "main/add_data.html", {"form": form})
    return HttpResponse("You don't authenticated!")


def del_data(request, db_name, id):
    delete_record(db_name, id)
    return redirect(f"/table_view/{db_name}")
