import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import BookAppointmentModel

# gets the current date so that ican disable the past date
current_date = str(datetime.date.today())


class BookAppointmentForm(forms.ModelForm):
    '''
    handels book appointment form
    '''

    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'name', 'email', 'created_date',
                  'treatments', 'your_request')

        labels = {
            'created_date': 'Request Date',
            'your_request': 'Message'
        }

        widgets = {
            'created_date': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    'minDate': current_date,
                }
            ),
            'your_request': forms.Textarea(attrs={'rows': 6, 'cols': 20,
                                                  'style': 'resize:none;'}),
        }
