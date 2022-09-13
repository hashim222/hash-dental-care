from django.shortcuts import render
from django.views.generic import ListView
from .models import Treatment

# Create your views here.


class OurTreatment(ListView):
    model = Treatment
    
    queryset = Treatment.objects.all()
    template_name = 'treatments.html'
    paginate_by = 6
