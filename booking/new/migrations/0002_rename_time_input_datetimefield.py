# Generated by Django 4.2.2 on 2023-06-07 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='time',
            new_name='datetimefield',
        ),
    ]
