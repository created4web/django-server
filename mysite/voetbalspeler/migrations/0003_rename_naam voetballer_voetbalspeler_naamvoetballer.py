# Generated by Django 3.2.18 on 2023-04-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voetbalspeler', '0002_rename_naamvoetballer_voetbalspeler_naam voetballer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voetbalspeler',
            old_name='Naam voetballer',
            new_name='naamVoetballer',
        ),
    ]
