from django import forms
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from .models import ContactModel


class ContactForm(forms.ModelForm):
    '''
    handling contact forms using Django widgets
    '''
    class Meta:
        model = ContactModel
        fields = (
            'name', 'email', 'phone'
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'}),
            'phone': RegionalPhoneNumberWidget(attrs={
                'placeholder': 'Phone',
                'error_messages': 'Incorrect'
            }),
        }

    def object(self):
        pass
