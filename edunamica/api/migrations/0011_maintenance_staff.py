# Generated by Django 5.1.2 on 2024-10-28 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_cleaning_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
                ('toolkit_provided', models.CharField(max_length=100)),
                ('Team_Members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
    ]
