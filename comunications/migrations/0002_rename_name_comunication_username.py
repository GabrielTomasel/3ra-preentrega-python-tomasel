# Generated by Django 4.2.2 on 2023-07-03 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunication',
            old_name='name',
            new_name='username',
        ),
    ]
