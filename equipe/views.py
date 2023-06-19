from django.shortcuts import render, redirect
from .models import Equipe
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
    return render(request, 'temp/addEquipe.html', {'form':form})