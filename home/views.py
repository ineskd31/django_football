from django.shortcuts import render
from joueur.models import Joueur
from equipe.models import Equipe


# Create your views here.
def home(request):
    allJoueur = Joueur.objects.all()
    allEquipe = Equipe.objects.all()
    joueurs = Joueur.objects.all()

    equipe_non_complete = Equipe.objects.all()[:2]

    joueur_sans_equipe = Joueur.objects.filter(equipe__isnull=True)[:4]

    joueur_equipe=Joueur.objects.all()[:4]

    equipes_europe = Equipe.objects.filter(continent__name="Europe")
    
    equipes_hors_europe = Equipe.objects.exclude(continent__name="Europe")

    context = {'joueurs':joueurs, "allJoueur":allJoueur, "allEquipe": allEquipe, 'enc':equipe_non_complete, 'jse':joueur_sans_equipe, 'je':joueur_equipe, 'ee':equipes_europe, 'ehe':equipes_hors_europe}

    return render(request, 'temp/home.html', context)