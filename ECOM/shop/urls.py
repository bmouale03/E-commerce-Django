from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
path('', views.shop, name='shop'),
path('panier/', views.panier, name='panier'), # voici la premiere fonction
path('commande/', views.commande, name='commande'), # voici la deuxieme fonction
]