
# views.py
from django.shortcuts import render, redirect
from .models import Commande,Car,Contact 
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.utils.html import escape
from django.shortcuts import get_object_or_404, render
from .models import Car

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    cars = Car.objects.all()
    # Voitures en vedette (peut être filtré selon certains critères)
    featured_cars = Car.objects.filter(featured=True) if 'featured' in request.GET else cars
    context = {
        'car': car,
        'cars': cars,
        'featured_cars': featured_cars,
    }
    
    return render(request, 'car_detail.html', context)







def home(request):
    query = request.GET.get('query', '')
    
    # Rechercher les voitures selon la marque ou le modèle correspondant à la requête
    results = Car.objects.filter(marque__icontains=query) | Car.objects.filter(modele__icontains=query) if query else Car.objects.none()
    
    # Toutes les voitures (pour la section "featured_cars")
    cars = Car.objects.all()
    
    featured_cars = Car.objects.filter(featured=True) if 'featured' in request.GET else cars
    
    # Contexte à passer au template
    context = {
        'query': query,
        'results': results,
        'no_results': not results.exists() and query,
        'cars': cars,
        'featured_cars': featured_cars,
    }
    
    return render(request, 'home.html', context)



def commande(request):
    cars = Car.objects.all()  # Par défaut, récupérer toutes les voitures
    if request.method == 'POST':
        nom_client = request.POST.get('nom_client')
        adresse = request.POST.get('adresse')
        car = request.POST.get('car')
        duration = request.POST.get('duration')
        email = request.POST.get('email')
        delivery = request.POST.get('delivery')
        number = request.POST.get('number')
        
        if nom_client and adresse and car and duration and email and number and delivery:
            commande = Commande(
                nom_client=nom_client,
                adresse=adresse,
                car=car,
                duration=duration,
                email=email,
                number=number,
                delivery=delivery
            )
            commande.save()
            success_message = "confirmer le payement "
            return render(request, 'success.html', {'success_message': escape(success_message), 'redirect_url': reverse('home')})
        else:
            error_message = "Veuillez remplir tous les champs du formulaire."
            return HttpResponse(error_message)
    featured_cars = Car.objects.all()  # Vous pouvez ajouter des filtres si nécessaire, par exemple : Car.objects.filter(featured=Tru
    context = {'cars': cars,  'featured_cars': featured_cars}
    return render(request, 'commande.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            contact = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact.save()
            return HttpResponse("Message envoyé  avec succès !")
        else:
            return HttpResponse("Veuillez remplir tous les champs du formulaire.")
    return render(request, 'contact.html')



