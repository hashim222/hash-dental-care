# Generated by Django 3.2.15 on 2022-09-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_rename_fullname_contactmodel_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'Contact Model'},
        ),
    ]
