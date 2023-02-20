from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #---------------------------
    #opcion 1 - create
    #comment=Comment(name="Juanjo", score=5, comment="Este es un comentario")
    #comment.save()
    #---------------------------
    #opcion 2 - create
    create=Comment.objects.create(name="Alex")
    #---------------------------
    return HttpResponse("Ruta para probar la creacion de modelos ")

def delete(request):
    #---------------------------
    #opcion 1 - delete
    #comment=Comment.objects.get(id=1)
    #comment.delete()
    #opcion 2 - delete
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para ptobar los borrados")
