from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.http import HttpResponseRedirect


class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    # def form_valid(self, form):
    #     form.cheese()
    #     return super().form_valid(form)
    def form_valid(self, form):
        form.object()
        messages.success(self.request, 'Form submission successful')
        return HttpResponseRedirect(self.request.path_info)
