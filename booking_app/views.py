from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class BookAppointments(TemplateView):
    template_name = 'book_appointments.html'


class Notifications(TemplateView):
    template_name = 'notifications.html'
