from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BookAppointmentForm
from django.views.generic.edit import FormView
# from django.contrib import messages
# from django.http import HttpResponseRedirect


class Home(TemplateView):
    '''
    home template view for the site
    '''
    template_name = 'home.html'


class BookAppointments(FormView):
    '''
    handels users book appointment 
    '''
    template_name = 'book_appointments.html'
    form_class = BookAppointmentForm
    success_url = '/book_appointments/'

    def form_valid(self, form):
        return super().form_valid(form)



class Notifications(TemplateView):
    template_name = 'notifications.html'
