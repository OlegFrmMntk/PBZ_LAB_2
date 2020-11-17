from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime


# Create your views here.
def index(request):
    return render(request, 'main.html', {'names': Owner.objects})


def owners(request):
    return render(request, 'menu_owner.html', {'owners': Owner.objects.all()})


def exhibitions(request):
    context = {'exhibitions': Exhibition.objects.all()}

    artworks = {}
    for exhibition in context['exhibitions']:
        artworks[exhibition] = Exhibition.objects.get(name=exhibition.name).artwork.all()
    context['artworks'] = artworks

    return render(request, 'menu_exhibition.html', context)


def exhibition_halls(request):
    return render(request, 'menu_exhibition_hall.html', {'exhibition_halls': ExhibitionHall.objects.all()})


def artists(request):
    return render(request, 'menu_artist.html', {'artists': Artist.objects.all()})


def artworks(request):
    return render(request, 'menu_artwork.html', {'artworks': Artwork.objects.all()})


def exhibitions_and_artists(request):
    context = {'flag': True}
    if request.method == 'POST':
        exhibition_name = request.POST['exhibition_name']
        try:
            exhibition = Exhibition.objects.get(name=exhibition_name)
        except:
            raise Exhibition('Выставок с данными названием не существует')

        context['exhibition'] = exhibition
        context['artworks'] = Exhibition.objects.get(name=exhibition.name).artwork.all()

        context['flag'] = False

        return render(request, 'exhibition_artist.html', context)
    else:
        return render(request, 'exhibition_artist.html', context)


def exhibition_hall_in_city(request):
    context = {'flag': True}
    if request.method == 'POST':
        city = request.POST['city_name']
        try:
            exhibition_halls = ExhibitionHall.objects.filter(address__contains=city)
        except:
            raise ExhibitionHall('Города с данным названием не существует')

        context['exhibition_halls'] = exhibition_halls
        context['flag'] = False

        return render(request, 'exhibition_hall_in_city.html', context)
    else:
        return render(request, 'exhibition_hall_in_city.html', context)


def now_exhibitions(request):
    now_date = datetime.datetime.now()
    exhibitions = Exhibition.objects.filter(start_date__lt=now_date.date(), end_date__gt=now_date.date())

    artworks = {}
    for exhibition in exhibitions:
        artworks[exhibition] = Exhibition.objects.get(name=exhibition.name).artwork.all()

    return render(request, 'now_exhibitions.html', {'exhibitions': exhibitions, 'artworks': artworks})
