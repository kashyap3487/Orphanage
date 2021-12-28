# Generated by Django 3.0.5 on 2021-12-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_management', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
