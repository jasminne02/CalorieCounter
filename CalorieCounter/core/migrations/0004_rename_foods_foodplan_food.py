# Generated by Django 4.1.3 on 2022-11-09 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_foodplan_foods'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodplan',
            old_name='foods',
            new_name='food',
        ),
    ]
