# Generated by Django 3.0.5 on 2021-12-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_management', '0007_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
