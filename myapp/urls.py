"""tuto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('match', views.match),
    path('add_vote1/<int:id>/', views.add_vote1),
    path('add_vote2/<int:id>/', views.add_vote2),
    path('connexion', views.connexion,name='connexion'),
    path('inscription', views.inscription,name='inscription'),
    path('verif', views.verif,name='verif'),
    path('deconnect', views.deconnect,name='deconnect'),
    path('inscript/', views.inscript, name='inscript'),

]