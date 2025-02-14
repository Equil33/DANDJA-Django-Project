from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
    path('produits/modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/supprimer/<int:pk>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('ventes/traiter/', views.traiter_vente, name='traiter_vente'),

    path('ventes/supprimer/<int:pk>/', views.supprimer_vente, name='supprimer_vente'),
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'), 
]
