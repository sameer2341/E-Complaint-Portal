# Generated by Django 3.0.5 on 2020-06-22 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculity', '0006_acomplaint_send_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejcomplaint',
            name='user',
        ),
    ]
