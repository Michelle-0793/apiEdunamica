# Generated by Django 5.1.2 on 2024-10-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_salon_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission_Slip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Permission_type', models.CharField(max_length=50)),
                ('Request_date', models.DateField()),
                ('Status', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
        ),
    ]
