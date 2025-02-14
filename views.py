from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produit, Categorie, Vente
from .forms import ProduitForm, CategorieForm, VenteForm 

def home(request):
    return render(request, 'home.html')

def supprimer_vente(request, pk):
    vente = Vente.objects.get(pk=pk)
    vente.delete()
    return redirect('tableau_de_bord')

def modifier_produit(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/modifier.html', {'form': form, 'produit': produit})

def liste_produits(request):
    search_query = request.GET.get('search', '')
    produits = Produit.objects.all()
    
    if search_query:
        produits = produits.filter(nom__icontains=search_query)

    return render(request, 'produits/liste.html', {'produits': produits, 'search_query': search_query})

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/ajouter.html', {'form': form})

def supprimer_produit(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/supprimer_produit.html', {'produit': produit})

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'produits/categories.html', {'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'produits/ajouter_categorie.html', {'form': form})

def supprimer_categorie(request, pk):
    categorie = Categorie.objects.get(pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'produits/supprimer_categorie.html', {'categorie': categorie})


def traiter_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            produit = vente.produit
            if produit.quantite_stock >= vente.quantite: 
                produit.quantite_stock -= vente.quantite  
                produit.save() 
                vente.prix_total = produit.prix * vente.quantite
                vente.mode_paye = form.cleaned_data['mode_paye'] 
                vente.save()  
                return redirect('tableau_de_bord') 
            else:
                return render(request, 'ventes/traiter.html', {'form': form, 'error': 'Stock insuffisant.', 'prix_total': vente.prix_total})
    else:
        form = VenteForm()
    return render(request, 'ventes/traiter.html', {'form': form})


def tableau_de_bord(request):
    ventes = Vente.objects.all()
    produits = Produit.objects.all() 
    return render(request, 'tableauDeBord/index.html', {'ventes': ventes, 'produits': produits})
