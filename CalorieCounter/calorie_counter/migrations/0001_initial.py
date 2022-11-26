# Generated by Django 4.1.3 on 2022-11-10 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_eaten', models.PositiveIntegerField(blank=True, null=True)),
                ('calories_burnt', models.PositiveIntegerField(blank=True, null=True)),
                ('fats_grams_per_day', models.PositiveIntegerField(blank=True, null=True)),
                ('proteins_grams_per_day', models.PositiveIntegerField(blank=True, null=True)),
                ('carbs_grams_per_day', models.PositiveIntegerField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]