# Generated by Django 3.1.3 on 2020-12-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abonent',
            old_name='StreetNM',
            new_name='StreetCD',
        ),
    ]
