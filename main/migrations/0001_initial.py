# Generated by Django 3.1.3 on 2020-12-09 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StreetName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Abonent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=15)),
                ('FlatNumber', models.IntegerField()),
                ('CountPerson', models.IntegerField()),
                ('Counter', models.BooleanField()),
                ('StreetNM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.street')),
            ],
        ),
    ]
