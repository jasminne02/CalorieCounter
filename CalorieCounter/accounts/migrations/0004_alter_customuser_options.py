# Generated by Django 4.1.3 on 2022-11-10 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_add_motivations_customuser_motivations_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('username',)},
        ),
    ]
