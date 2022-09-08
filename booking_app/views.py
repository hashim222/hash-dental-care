from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class test_if_templates_works(TemplateView):
    template_name = 'base.html'

