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

    template_name = 'book_appointments.html'
    form_class = BookAppointmentForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.send_form()
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     print(form.errors)


class Notifications(TemplateView):
    template_name = 'notifications.html'
