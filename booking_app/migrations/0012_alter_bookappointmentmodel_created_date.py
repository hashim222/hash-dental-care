# Generated by Django 3.2.15 on 2022-09-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0011_alter_bookappointmentmodel_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointmentmodel',
            name='created_date',
            field=models.DateField(),
        ),
    ]