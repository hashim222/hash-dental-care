from django.urls import path
from .views import OurTreatment

urlpatterns = [
    path('treatments/', OurTreatment.as_view(), name='treatments'),
]
