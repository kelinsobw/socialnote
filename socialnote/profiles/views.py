import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profiles_index(request):
    return HttpResponse("Profiles index view")
