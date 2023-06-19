from django.db import models

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Equipe(models.Model):
    name = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    # maxJoueur = models.IntegerField()
    
    def __str__(self):
        return self.name
