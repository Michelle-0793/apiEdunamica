# Generated by Django 5.1.2 on 2024-10-28 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_administrative_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(max_length=100)),
                ('assigned_area', models.CharField(max_length=100)),
                ('Team_Members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
    ]
