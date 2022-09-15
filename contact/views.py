from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.http import HttpResponseRedirect


class ContactUs(FormView):
    '''
    handels user input data and sends them back a message 
    '''
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.object()
        messages.success(self.request, "Thank you for contacting us, we'll get back to you as soon as possible.")
        return HttpResponseRedirect(self.request.path_info)

