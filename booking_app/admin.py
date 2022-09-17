from django.contrib import admin
from .models import BookAppointmentModel


@admin.register(BookAppointmentModel)
class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'phone', 'created_date',
                    'your_request', 'treatments')
    list_filter = ('status', 'created_date')
    search_fields = ['name']
    actions = ['approve_request']

    def approve_request(self, request, queryset):
        queryset.update(status=1)
