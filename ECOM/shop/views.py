from django.shortcuts import render

# Create your views here.
def shop(request, *args, **kwargs):
    """ vue principale """
    context = {}
    return render(request, 'shop/index.html', context)

def panier(request, *args, **kwargs):
    """ panier """
    context = {}
    return render(request, 'shop/panier.html', context)

def commande(request, *args, **kwargs):
    """ Commande """
    context = {}
    return render(request, 'shop/commande.html', context)
