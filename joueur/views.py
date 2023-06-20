from django.shortcuts import render,redirect
from .models import Joueur
from .forms import JoueurForm

# Create your views here.
def addJoueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JoueurForm()
    return render(request, 'temp/joueur/addJoueur.html', {'form':form})

