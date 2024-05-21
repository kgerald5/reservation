from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import  Commande, Car, Contact

admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'date_commande')

admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('marque' , 'modele')

admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email')   
    


admin.site.register(Contact, ContactAdmin)
admin.site.register(Car, CarAdmin) 
admin.site.register(Commande, CommandeAdmin)  # Alternative way to register



