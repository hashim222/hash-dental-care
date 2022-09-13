from django.urls import path
from .views import OurTreatments

urlpatterns = [
    path('treatments/', OurTreatments.as_view(), name='treatments'),
]
