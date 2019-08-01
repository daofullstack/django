from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Page admin Parisport" 
admin.site.site_title = "Jamais perdre"
admin.site.index_title = "Acceuil"

@admin.register(Match) # on met le nom du modele
class MatchAdmin(admin.ModelAdmin):
    list_display = ('descript_match' ,'equipe1','equipe2','vote1','vote2','date_add','date_exp','statut',)
    list_filter = ("date_add","statut",) #fitrer par champ
    search_fields = ('equipe1' ,'equipe2',) # rechercher selon un champ
    list_per_page = 50 # paginatio

    ordering = ['-statut', '-date_add','-date_exp']  #ordonner par 

@admin.register(Sports) # on met le nom du modele
class SportsAdmin(admin.ModelAdmin):
    list_display = ('type_sport' ,'created_at','updated_at','statut',)
    list_filter = ("created_at","statut",) #fitrer par champ
    search_fields = ('type_sport' ,'created_at',) # rechercher selon un champ
    list_per_page = 50 # paginatio

    ordering = ['-statut', '-type_sport']  #ordonner par 

@admin.register(Utilisateur) # on met le nom du modele
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom' ,'prenom','username','compte','email','date_add',)
    

      

