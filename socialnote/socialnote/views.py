import logging

from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from profiles.models import Profile
from socialnote.forms import RegisterForm, RegisterForm_2, LoginForm

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            user = User(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("register_2")
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form})


def register_2(request):
    if request.method == "POST":
        form = RegisterForm_2(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            profiles = Profile(
                user=settings.AUTH_USER_MODEL,
                age=form.cleaned_data["age"],
                gender=form.cleaned_data["gender"],
                user_image=form.cleaned_data["user_image"],
                country=form.cleaned_data["country"]
            )
            profiles.save()
            return redirect("register")
    else:
        form = RegisterForm_2()
    return render(request, "main/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            user = authenticate(username="harelik", password="Kirito_sun7")
        return redirect("/home/")
    else:
        form = LoginForm()
    return render(request, "main/login.html", {"form": form})
