from django import forms


class DatePicker(forms.DateInput):
    '''
    user can input their dates
    '''
    input_type = 'date'