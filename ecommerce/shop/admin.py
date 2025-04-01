from django.contrib import admin
from .models import Category , Product, Commande,Contact,UserProfile

# Register your models here.
admin.site.site_header = "E-commerce ChineAfrica"
admin.site.site_title ="ChineAfrica"
admin.site.index_title = "Espace Manageur Principal"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    search_fields=('title',)
 
    
class AdminProduct(admin.ModelAdmin):
    list_display=('title' , 'price', 'category', 'date_added')
    search_fields=('title',)
    list_editable=('price',)
    
class AdminCommande(admin.ModelAdmin):
    list_display=('items', 'nom', 'email', 'address', 'pays', 'total','date_commande')
    search_fields=('nom','date_commande', )
    
class AdminContact(admin.ModelAdmin):
   list_display=('name', 'email', 'subject', 'message', 'created_at')
   search_fields=('email', )

class AdminUserProfile(admin.ModelAdmin):
    list_display=('user', 'phone_number')
    search_fields=('email', )
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategorie)
admin.site.register(Commande, AdminCommande)
admin.site.register(Contact, AdminContact)
admin.site.register(UserProfile, AdminUserProfile)




