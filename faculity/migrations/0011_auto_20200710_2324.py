# Generated by Django 3.0.5 on 2020-07-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculity', '0010_remove_acomplaint_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acomplaint',
            old_name='send',
            new_name='forward',
        ),
    ]