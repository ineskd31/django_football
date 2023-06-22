from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipe
from joueur.models import Joueur
from .forms import EquipeForm

# Create your views here.
def addEquipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipeForm()
    return render(request, 'temp/equipe/addEquipe.html', {'form':form})



def editEquipe(request,id):
    edit = Equipe.objects.get(id=id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipeForm(instance=edit)
    return render(request, 'temp/equipe/editEquipe.html', {'form': form})



def showEquipe(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    joueurs = Joueur.objects.filter(equipe=equipe)
    context = {'equipe': equipe, 'joueurs': joueurs}
    return render(request, 'temp/equipe/showEquipe.html', context)