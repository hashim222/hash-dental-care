import datetime
from django.forms import ModelForm
from .models import BookAppointmentModel
from bootstrap_datepicker_plus.widgets import DatePickerInput


class BookAppointmentForm(ModelForm):
    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'name', 'email', 'created_date',
                  'treatments', 'your_request')

        current_date = str(datetime.date.today())

        widgets = {
            'created_date': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    'minDate': current_date
                }
            )
        }

        def send_form(self):
            pass
