from django.shortcuts import render
from django.views.generic import TemplateView


class ContactUs(TemplateView):
    template_name = 'contact.html'