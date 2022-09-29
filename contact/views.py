from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import ContactForm


class ContactUs(FormView):
    '''
    Sends back a message to users who fill out a contact form
    '''
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.object()
        messages.success(
            self.request,
            "Thank you for contacting us, we'll get back to \
                you as soon as possible.")
        return HttpResponseRedirect(self.request.path_info)
