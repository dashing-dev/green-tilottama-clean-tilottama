# Generated by Django 4.2.2 on 2023-06-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0005_alter_input_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='description',
            field=models.CharField(max_length=350),
        ),
    ]
