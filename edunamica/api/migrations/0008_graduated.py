# Generated by Django 5.1.2 on 2024-10-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_partnership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Graduated_name', models.CharField(max_length=100)),
                ('Graduated_lastname', models.CharField(max_length=100)),
                ('Course_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=255)),
                ('Graduation_date', models.DateField()),
            ],
        ),
    ]
