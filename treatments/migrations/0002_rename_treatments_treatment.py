# Generated by Django 3.2.15 on 2022-09-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Treatments',
            new_name='Treatment',
        ),
    ]