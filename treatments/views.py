from django.shortcuts import render
from django.views.generic import ListView
from .models import Treatment

# Create your views here.


class OurTreatment(ListView):
    '''
    display treatments images, title, descriptions and prices for the website
    '''
    model = Treatment

    queryset = Treatment.objects.all()
    template_name = 'treatments.html'
