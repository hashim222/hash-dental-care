from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class OurTreatments(TemplateView):
    template_name = 'treatments.html'