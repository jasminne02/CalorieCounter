# Generated by Django 4.1.3 on 2022-11-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_motivations_motivation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='burnt_calories_per_min',
            new_name='metabolic_equivalent',
        ),
    ]
