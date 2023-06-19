from django.shortcuts import render
from joueur.models import Joueur
from equipe.models import Equipe


# Create your views here.
def home(request):
    allJoueur = Joueur.objects.all()
    allEquipe = Equipe.objects.all()
    return render(request, 'temp/home.html', {"allJoueur":allJoueur, "allEquipe": allEquipe})