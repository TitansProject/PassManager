from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from PassManagerApp.models import Wifi


def index(request):
    wifis = Wifi.objects.all()
    template = loader.get_template('PassManagerApp/index.html')
    context = {
        'wifis': wifis,
    }
    return HttpResponse(template.render(context, request))
