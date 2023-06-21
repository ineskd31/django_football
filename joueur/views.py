from django.shortcuts import render,redirect
from .models import Joueur
from .forms import JoueurForm

# Create your views here.

def addJoueur(request):
    if request.method == "POST":
        form = JoueurForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            team = form.cleaned_data['equipe']
            num_players = Joueur.objects.filter(equipe=team).count()

            #? Max players by role
            if team:
                role = player.role
                if role != 'Remplacant' and team.joueur_set.filter(role=role).count() >= 4:
                    error_message = f"L'équipe {team.club} a déjà atteint le maximum de joueurs pour le rôle {role}."
                    return render(request, 'temp/joueur/addJoueur.html', {'form': form, 'error_message': error_message})

            #? Max players by team
            if num_players >= 12:
                error_max_players = f"L'équipe {team.club} est déjà complète. Veuillez en choisir une autre."
                return render(request, 'temp/joueur/addJoueur.html', {'form': form, 'error_max_players': error_max_players})

            player.team = team
            player.save()

            return redirect("home")
    else:
        form = JoueurForm()
    return render(request, "temp/joueur/addJoueur.html", { "form": form })