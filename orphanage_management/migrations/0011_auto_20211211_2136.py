# Generated by Django 3.0.5 on 2021-12-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_management', '0010_auto_20211210_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=25)),
                ('language', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]