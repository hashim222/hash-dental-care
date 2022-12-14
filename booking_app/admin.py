'''
Booking_app admin
'''
from django.contrib import admin
from .models import BookAppointmentModel


@admin.register(BookAppointmentModel)
class BookAppointmentAdmin(admin.ModelAdmin):
    '''
    Created a custom admin page to simplify admin tasks
    and give admins more control over the users.
    '''
    list_display = ('title', 'name', 'email', 'created_date',
                    'your_request', 'update_date', 'treatments', 'status')
    list_filter = ('admin_decision', 'created_date')
    search_fields = ['name']
    actions = ['approve_request']

    def approve_request(self, request, queryset):
        '''
        Handels status choices
        '''
        queryset.update(status=1)
