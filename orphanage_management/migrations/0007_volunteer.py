# Generated by Django 3.0.5 on 2021-12-05 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_management', '0006_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=25)),
                ('language', models.CharField(max_length=15)),
                ('mobile_no', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='')),
                ('password', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=25)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orphanage_management.City')),
            ],
        ),
    ]
