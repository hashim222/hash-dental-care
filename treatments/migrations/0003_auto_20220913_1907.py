# Generated by Django 3.2.15 on 2022-09-13 19:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0002_rename_treatments_treatment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='treatment',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
