from django.db import models,transaction
from django.db.models import F
from django import forms
#from .models import Utilisateur
from .models import *

# Create your models here.
class Sports(models.Model):
    type_sport= models.CharField(max_length=250,verbose_name="type de sport")
    statut=  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Match(models.Model):
    descript_match= models.CharField(max_length=250,verbose_name="X face à Y")
    equipe1= models.CharField(max_length=100)
    equipe2= models.CharField(max_length=100)
    vote1 =  models.IntegerField(default=0)
    vote2 =  models.IntegerField(default=0)
    date_add= models.DateTimeField(auto_now_add=True)
    date_exp = models.DateTimeField(auto_now=True)
    statut=  models.BooleanField(default=True)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE,related_name="sport_match", null=True)
class Utilisateur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    compte =  models.IntegerField(default=10000)
    date_add= models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields =['prenom', 'nom','username','email', 'password',]