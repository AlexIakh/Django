from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurante

def create(request):
    place=Place(name="Lugar 1", address="Calle Demo")
    place.save()

    restaurant=Restaurante(place=place, number_of_employees=8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
