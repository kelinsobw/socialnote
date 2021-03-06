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


# Retrieves the tables of the current user from
# the database and sends them to FRONTEND
def my_list(request):
    try:
        bases = Databases.objects.filter(author=request.user).order_by("-created_at")
    except:
        return HttpResponse("No data available")
    return render(request, "main/my_list.html", {"bases": bases})


# Retrieves tables of all users from the
# database and sends them to FRONTEND
def index(request):
    bases = list(Privates.objects.filter(privates="None").values())
    print(bases)
    base_id = []
    for elements in bases:
        if elements.get("privates") == "None":
            base_id.append(elements.get("base_id"))
    print(base_id)
    bases = Databases.objects.filter(id__in=base_id)
    return render(request, "main/list.html", {"bases": bases})


# The function creates a new table
# according to the parameters set by the user
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


# Retrieves from the database records of their specific database
def table_view(request, db_name):
    bases_res = []
    name = []
    name.append(db_name)
    bases = get_the_date(db_name)
    bases_temp_1 = bases[1]
    bases_temp_1 = bases_temp_1[0]
    for i in range(0, len(bases_temp_1) - 1):
        name.append(" ")
    bases_res.append(name)
    bases_res.append(list(bases[0]))
    for element in bases_temp_1:
        bases_res.append(list(element))
    bases = bases_res
    return render(request, "main/table_view.html", {"bases": bases})


# Function for adding data to the database
def add_data(request, db_name):
    base_author = Databases.objects.filter(db_name=db_name, author=request.user).values()
    if len(base_author) == 1:
        # A dynamic form for adding data to a table. It has 8 fields, the required number is used on the frontend
        class Forms_add(forms.Form):
            types = view_column_type(db_name)
            try:
                base_1 = forms.CharField(label=types[1])
            except:
                pass
            try:
                base_2 = forms.CharField(label=types[2])
            except:
                pass
            try:
                base_3 = forms.CharField(label=types[3])
            except:
                pass
            try:
                base_4 = forms.CharField(label=types[4])
            except:
                pass
            try:
                base_5 = forms.CharField(label=types[5])
            except:
                pass
            try:
                base_6 = forms.CharField(label=types[6])
            except:
                pass
            try:
                base_7 = forms.CharField(label=types[7])
            except:
                pass

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
    else:
        return redirect("/error")


# The function deletes a specific record in a specific table
def del_data(request, db_name, id):
    delete_record(db_name, id)
    return redirect(f"/table_view/{db_name}")


def error_access(request):
    return render(request, "main/error.html")
