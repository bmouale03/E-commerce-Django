from django.urls import path
from shop.views import index, detail, checkout,confirmation,contact_view,success_view
from .import views
from .views import register, login_view

urlpatterns = [
    path('' , index, name='base'),
    path('<int:myid>', detail, name='detail'),
    path('checkout', checkout, name='checkout'),
    path('confirmation', confirmation, name="confirmation" ),
    path('contact/', contact_view, name='contact'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),


]
