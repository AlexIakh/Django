from multiprocessing.spawn import old_main_modules
from django.db import models as m

class Place(m.Model):
    name=m.CharField(max_length=50)
    address=m.CharField(max_length=80)

    def __str__(self):
        return self.name

class Restaurante(m.Model):
    place=m.OneToOneField(Place, on_delete=m.CASCADE, primary_key=True)
    number_of_employees=m.IntegerField(default=1)

    def __str__(self):
        return self.place.name


