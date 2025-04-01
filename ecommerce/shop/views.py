from django.shortcuts import render, redirect
from .models import Product, Category, Commande,Contact
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import UserProfile


# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')#Pour afficher tous les produits
    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name) #Pour rechercher un produit
    paginator = Paginator(product_object,4)
    page = request.GET.get('page')
    product_object=paginator.get_page(page)# Pour faire la pagination
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

def checkout(request):
    if request.method =="POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom =request.POST.get('nom')
        email =request.POST.get('email')
        address =request.POST.get('address')
        ville =request.POST.get('ville')
        pays =request.POST.get('pays')
        zipcode =request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
        
    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name':nom})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')  # Redirection après soumission
    else:
        form = ContactForm()
    return render(request, 'shop/contact_form.html', {'form': form})
    
def success_view(request):
    return render(request, 'shop/contact_success.html') 

# Inscription
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, phone_number=form.cleaned_data['phone_number'])
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'shop/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})