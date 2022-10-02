'''
Booking_app Views
'''
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookAppointmentForm
from .models import BookAppointmentModel


class Home(generic.TemplateView):
    '''
    Hisplay home view for the site
    '''
    template_name = 'home.html'


class BookAppointments(CreateView):
    '''
    After submitting the form user details will be saved in the database
    and users will be redirected to the manage booking page.
    '''
    template_name = 'book_appointments.html'
    form_class = BookAppointmentForm

    def form_valid(self, form):
        form.instance.patient = self.request.user
        form.save()
        messages.success(
            self.request,
            'Your request has been submitted and is awaiting for approval')
        return HttpResponseRedirect('/manage_bookings/')


class ManageBooking(generic.ListView):
    '''
    Retrieves data from the database and displays it in
    the manage_bookings page.
    '''
    model = BookAppointmentModel
    template_name = 'manage_bookings.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = context['object_list']
        return context

    def get_queryset(self):
        return BookAppointmentModel.objects.filter(
            patient=self.request.user).order_by("created_date")


class DeleteAppointment(DeleteView):
    '''
    Handles the delete option for users, letting them
    cancel their appointment if they wish.
    '''
    model = BookAppointmentModel
    success_url = '/manage_bookings/'
    template_name = "confirm_delete.html"

    def delete_appointment(self, request, pk, *args, **kwargs):
        '''
        methods handels delete
        '''
        appointments = BookAppointmentModel.objects.get(
            pk=self.request.pk)
        appointments.delete()


class UpdateAppointment(UpdateView):
    '''
    Handels update, if user wants to make any changes in already
    created appointment
    '''
    model = BookAppointmentModel
    template_name = 'update_appointments.html'
    form_class = BookAppointmentForm
    success_url = '/manage_bookings/'
