# Generated by Django 4.2.2 on 2023-06-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_rename_time_input_datetimefield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='datetimefield',
            new_name='time',
        ),
    ]
