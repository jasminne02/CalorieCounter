# Generated by Django 4.1.3 on 2022-11-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_foods_foodplan_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=450)),
                ('description', models.TextField()),
            ],
        ),
    ]
