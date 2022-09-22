from django.urls import path
from .views import Home, BookAppointments, Notifications, DeleteAppointment


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('book_appointments/', BookAppointments.as_view(),
         name='book_appointments'),
    path('notifications/', Notifications.as_view(), name='notifications'),
    path('delete/<int:pk>', DeleteAppointment.as_view(), name='delete'),
]
