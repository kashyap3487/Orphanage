# Generated by Django 3.0.5 on 2021-12-16 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage_management', '0012_auto_20211211_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='title',
        ),
    ]
