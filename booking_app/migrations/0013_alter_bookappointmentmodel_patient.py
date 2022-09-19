# Generated by Django 3.2.15 on 2022-09-19 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_app', '0012_alter_bookappointmentmodel_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointmentmodel',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL),
        ),
    ]