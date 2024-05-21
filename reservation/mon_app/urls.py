from django.urls import path
from . import views
from .views import commande, contact, car_detail
urlpatterns = [
    path('', views.home, name='home'),
    path('commande/', commande, name='commande'),
    path('contact/', contact, name='contact'),
    path('car/<int:id>/', car_detail, name='car_detail'),
    
]
