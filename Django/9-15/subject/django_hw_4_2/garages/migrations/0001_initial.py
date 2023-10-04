# Generated by Django 4.2.2 on 2023-09-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
                ('is_parking_avaliable', models.BooleanField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
    ]