# Generated by Django 5.1.3 on 2024-11-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_data', '0004_servicerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='client_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]