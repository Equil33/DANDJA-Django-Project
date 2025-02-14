from django import forms
from .models import Produit, Categorie, Vente

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'categorie', 'prix', 'quantite_stock']

class VenteForm(forms.ModelForm):


    PAYMENT_METHOD_CHOICES = [
        ('liquide', 'Liquide'),
        ('TMoney', 'TMoney'),
        ('Flooz', 'Flooz'),
    ]
    mode_paye = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, required=True)

    class Meta:
        model = Vente
        fields = ['produit', 'quantite', 'mode_paye']
