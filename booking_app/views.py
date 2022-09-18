from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookAppointmentForm
from django.views.generic.edit import FormView


class Home(TemplateView):
    '''
    home template for the site
    '''
    template_name = 'home.html'


class BookAppointments(FormView):
    template_name = 'book_appointments.html'
    form_class = BookAppointmentForm
    success_url = 'book_appointments/'

    def send(self, form):
        form.send_form()
        return super().form_valid(form)


class Notifications(TemplateView):
    template_name = 'notifications.html'
