# Generated by Django 3.2.15 on 2022-09-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_bookappointmentmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookappointmentmodel',
            options={'ordering': ['-created_date']},
        ),
    ]