from django.db import models
from equipe.models import Equipe

# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Joueur(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    image = models.URLField()
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE)
    


