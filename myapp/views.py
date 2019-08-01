from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.db.models import F
from django.http import HttpResponse
#from myapp.models import Match

# Create your views here.
def home(request):
    data={
        'nom':'dao',
        'prenom':'lassina'
    }
    return render(request,'myapp/index.html',data)

def match(request):
    utilisateurs=Utilisateur.objects.all()
    sports=Sports.objects.all()
    data={
        'sports':sports,
        'utilisateurs':utilisateurs,
    }
    return render(request,'myapp/match.html',data)
def add_vote1(request,id):
    id=id
    Match.objects.filter(id=id).update(vote1=F('vote1') + 1)
    return redirect('../../match')
def add_vote2(request,id):
    id=id
    Match.objects.filter(id=id).update(vote2=F('vote2') + 1)
    return redirect('../../match')


def connexion(request):
    return render(request,'myapp/connexion.html')

def inscription(request):
    return render(request,'myapp/inscription.html')

def inscript(request):
    prenom=request.POST['prenom']
    nom=request.POST['nom']
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    data={
        'prenom':prenom,
        'nom':nom,
        'username':username,
        'email':email,
        'password':password,
    }
    form = UtilisateurForm(data)
    if form.is_valid():
        form.save()
        return redirect('connexion')
    else:
        return redirect('inscription')
   

def verif(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/match')
    else:
        return redirect('/inscription')

def deconnect(request):
    logout(request)
    return redirect('../')
    