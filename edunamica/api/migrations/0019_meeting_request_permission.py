# Generated by Django 5.1.2 on 2024-10-28 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_early_exit_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Request_Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=100)),
                ('requested_by', models.CharField(max_length=50)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_requests', to='api.permission_slip')),
            ],
        ),
    ]
