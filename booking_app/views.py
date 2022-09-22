from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BookAppointmentForm
from .models import BookAppointmentModel


class Home(generic.TemplateView):
    '''
    home template view for the site
    '''
    template_name = 'home.html'


class BookAppointments(CreateView):
    '''
    after submiting the form user details will be saved on the database
    '''
    template_name = 'book_appointments.html'
    form_class = BookAppointmentForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Your request has been submitted and is awaiting for approval')
        return HttpResponseRedirect('/notifications/')


class Notifications(generic.ListView):
    '''
    gets data from the database and displays inside the notifications template
    '''
    model = BookAppointmentModel
    template_name = 'notifications.html'

    def get(self, request, *args, **kwargs):
        appointments = BookAppointmentModel.objects.all()
        form = BookAppointmentForm()
        context = {
            'appointments': appointments,
            'form': form
        }
        return render(request, self.template_name, context)


class DeleteAppointment(DeleteView):
    '''
    handels the delete option for user's where user can decide to delete appointment or not 
    '''
    model = BookAppointmentModel
    success_url = '/notifications/'
    template_name = "confirm_delete.html"

    def delete_appointment(self, request, pk, *args, **kwargs):
        appointments = BookAppointmentModel.objects.get(pk=self.request.pk)
        appointments.delete()
