'''
Contact forms
'''
from django import forms
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from .models import ContactModel


class ContactForm(forms.ModelForm):
    '''
    Modelform handels contact forms.
    To display forms better, added Django widgets attributes.
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
            }),
        }

    def object(self):
        pass
