# Generated by Django 5.1.2 on 2024-10-28 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_coworking_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon_Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('audio_video_equipment', models.BooleanField(default=False)),
                ('seating_arrangement', models.CharField(max_length=100)),
                ('Reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
            ],
        ),
    ]
