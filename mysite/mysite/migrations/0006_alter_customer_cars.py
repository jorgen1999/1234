# Generated by Django 4.0.1 on 2022-11-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_car_year_alter_customer_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cars',
            field=models.IntegerField(default=1),
        ),
    ]
