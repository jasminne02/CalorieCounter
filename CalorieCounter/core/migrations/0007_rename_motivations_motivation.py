# Generated by Django 4.1.3 on 2022-11-10 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_exercise_options_alter_food_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Motivations',
            new_name='Motivation',
        ),
    ]
