# Generated by Django 4.1.3 on 2022-11-10 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_motivations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='motivations',
            options={'ordering': ('pk',)},
        ),
    ]
