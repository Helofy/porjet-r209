from django.shortcuts import render
from .forms import ClubForm
from . import models

def index(request):

    return render(request, 'football/index.html')




def ajout(request):
    if request.method == "POST":
        form = ClubForm(request)
        if form.is_valid():
            club = form.save()
            return render(request, "/football/affiche.html", {"club": club})
        else:
            return render(request, "football/ajout.html", {"form": form})

    else:
        form = ClubForm()
        return render(request, "football/ajout.html", {"form": form})




def traitement(request):
    cform = ClubForm(request.POST)
    if cform.is_valid():
        club = cform.save()
        return render(request,"/football/affiche.html",{"club" : club})
    else:
        return render(request,"football/ajout.html",{"form": cform})
