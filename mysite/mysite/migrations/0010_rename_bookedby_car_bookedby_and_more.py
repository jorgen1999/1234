# Generated by Django 4.0.1 on 2022-11-03 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_car_bookedby_customer_bookcar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='bookedby',
            new_name='bookedBy',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='bookcar',
            new_name='bookedCar',
        ),
    ]