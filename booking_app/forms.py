from django.forms import ModelForm
from .models import BookAppointmentModel


class BookAppointmentForm(ModelForm):
    class Meta:
        model = BookAppointmentModel
        fields = ('title', 'name', 'phone',
                  'treatments', 'your_request')

        def send_form(self):
            pass


# from django import forms
# from .models import BookAppointmentModel


# class BookAppointmentForm(forms.Form):
#     name = forms.CharField(max_length=100)

#     def send_form(self):
#         pass
