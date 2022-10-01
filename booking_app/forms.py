'''
booking_app forms
'''
import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import BookAppointmentModel

# gets the current date so that ican disable the past date
CURRENT_DATE = str(datetime.date.today())


class BookAppointmentForm(forms.ModelForm):
    '''
    handels book appointment form.
    The Bootstrap datepicker library was installed, which makes
    form looks more appealing
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
                    'minDate': CURRENT_DATE,
                }
            ),
            'your_request': forms.Textarea(attrs={'rows': 6, 'cols': 20,
                                                  'placeholder':
                                                  'Message(optional)',
                                                  'style': 'resize:none;'},
                                           ),
        }
