from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    
    art1=Article(headline="Articulo primero")
    art1.save()
    art2=Article(headline="Articulo segundo")
    art2.save()
    art3=Article(headline="Articulo tercero")
    art3.save()

    pub1=Publication(title="Publicacion primera")
    pub1.save()
    pub2=Publication(title="Publicacion segunda")
    pub2.save()
    pub3=Publication(title="Publicacion tercera")
    pub3.save()
    pub4=Publication(title="Publicacion curta")
    pub4.save()
    pub5=Publication(title="Publicacion quinta")
    pub5.save()
    pub6=Publication(title="Publicacion sexta")
    pub6.save()
    pub7=Publication(title="Publicacion septima")
    pub7.save()

    art1.publication.add(pub1)
    art1.publication.add(pub2)
    art1.publication.add(pub3)
    art2.publication.add(pub4)
    art2.publication.add(pub5)
    art3.publication.add(pub6)
    art3.publication.add(pub7)

    result=art1.publication.all()
    
    #art1.publication.remove(pub1)

    #pub1=Publication.objects.get(id=1)
    result=pub1.article_set.all()


    return HttpResponse(result)
