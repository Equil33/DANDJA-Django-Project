from django.contrib import admin
from .models import Produit, Categorie, Vente

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Vente)
