from django.urls import path
from .views import Home, BookAppointments, ContactUs, Notifications


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('book_appointments/', BookAppointments.as_view(),
         name='book_appointments'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('notifications/', Notifications.as_view(), name='notifications'),
]
