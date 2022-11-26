# Generated by Django 4.1.3 on 2022-11-10 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_calories_per_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(default=55, error_messages={'min_value': 'Please enter a valid weight!'}, validators=[django.core.validators.MinValueValidator(30)]),
            preserve_default=False,
        ),
    ]