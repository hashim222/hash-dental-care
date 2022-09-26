from django.urls import path
from .views import Home, BookAppointments, ManageBooking,\
     DeleteAppointment, UpdateAppointment


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('book_appointments/', BookAppointments.as_view(),
         name='book_appointments'),
    path('manage_bookings/', ManageBooking.as_view(), name='manage_bookings'),
    path('delete/<int:pk>', DeleteAppointment.as_view(), name='delete'),
    path('update_appointment/<int:pk>', UpdateAppointment.as_view(),
         name='update_appointment')
]
