from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

def update(request):
    author=Author.objects.get(id=1)
    author.name="Juanjo"
    author.email="juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")


def queries(request):
    #Obtener todos los elementos
    authors=Author.objects.all()

    #Obtener datos filtrados por condicion
    filtered=Author.objects.filter(email='dawn46@example.com')

    #Obtener un unico objeto (filtrado)
    author=Author.objects.get(id=1)

    #Obtener los 10 primeros valores
    limits=Author.objects.all()[:10]

    #Obtener 5 elementos saltando los 5 promeros
    offsets=Author.objects.all()[5:10]

    #Obtener todos los elementos ordenados
    orders=Author.objects.all().order_by('email')

    #Obtener todos los cuyo id sea menor o igual a 15
    filtered2=Author.objects.filter(id__lte=15)

    #Obtener todos los authores que contienen en su nombre palabre yes
    filtered3=Author.objects.filter(name__contains="no")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered':filtered, 'author':author, 'limits':limits, 'offsets':offsets, 'orders':orders, 'filtered2':filtered2, 'filtered3':filtered3})

