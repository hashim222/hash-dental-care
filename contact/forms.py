from django import forms


class ContactForm(forms.Form):
    '''
    contact forms handling using Django widgets
    '''
    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(
        max_length=50, label='Email', widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=11, min_length=11,
                            label='Phone', widget=forms.TextInput(
                                attrs={'placeholder': 'Phone'}))

    def object(self):
        pass
