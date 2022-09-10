from django.urls import path
from .views import Home, OurTreatments, BookAppointments, ContactUs, Notifications


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('treatments/', OurTreatments.as_view(), name='treatments'),
    path('book_appointments/', BookAppointments.as_view(),
         name='book_appointments'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('notifications/', Notifications.as_view(), name='notifications'),
]
