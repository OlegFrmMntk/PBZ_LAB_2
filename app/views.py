from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return render(request, 'main.html', {'names': Owner.objects})


def owners(request):
    return render(request, 'menu_owner.html', {'owners': Owner.objects.all()})
