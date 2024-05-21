from django.db import models

# Create your models here.


class Commande(models.Model):
    nom_client = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    car = models.CharField(max_length=100)
    duration = models.IntegerField()
    email = models.TextField()
    number =models.CharField( max_length=11)
    delivery =models.DateField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_client
    

class Car(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    free =models.BooleanField(default=True)
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.price})"






class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    

    def __str__(self):
        return self.name