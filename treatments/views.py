'''
Treatments views
'''
from django.views.generic import ListView
from .models import Treatment


class OurTreatment(ListView):
    '''
    Display treatments images, title, descriptions and prices for the website
    '''
    model = Treatment

    queryset = Treatment.objects.all()
    template_name = 'treatments.html'
