from django.shortcuts import render,redirect
from .models import Joueur
from .forms import JoueurForm

# Create your views here.
def joueurs(request):
    allJoueur = Joueur.objects.all()
    return render(request, 'temp/home.html')