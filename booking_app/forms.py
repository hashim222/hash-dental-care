from django.forms import ModelForm
from .models import BookAppointmentModel
from .widgets import DatePicker


class BookAppointmentForm(ModelForm):
    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'name', 'email', 'created_date',
                  'treatments', 'your_request')

        widgets = {
            'created_date': DatePicker()
        }

        def send_form(self):
            pass
