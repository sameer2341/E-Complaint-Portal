# Generated by Django 3.0.5 on 2020-07-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculity', '0008_solcomplaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='acomplaint',
            name='send',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
