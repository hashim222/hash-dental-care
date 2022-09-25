from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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
        form.instance.patient = self.request.user
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
    paginate_by = 6
    # some_property = "appointements"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = context['object_list']
        return context

    def get_queryset(self):
        return BookAppointmentModel.objects.filter(
            patient=self.request.user).order_by("created_date")


class DeleteAppointment(DeleteView):
    '''
    handels the delete option for user's where user can decide to cancel an appointment or not
    '''
    model = BookAppointmentModel
    success_url = '/notifications/'
    template_name = "confirm_delete.html"

    def delete_appointment(self, request, pk, *args, **kwargs):
        appointments = BookAppointmentModel.objects.get_object_or_404(
            pk=self.request.pk)
        appointments.delete()


class UpdateAppointment(UpdateView):
    '''
    handels if user wants to make changes they already created
    '''
    model = BookAppointmentModel
    template_name = 'update_appointments.html'
    form_class = BookAppointmentForm
    success_url = '/notifications/'
