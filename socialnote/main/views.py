import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)

def index(request):
    return render(request, "")
