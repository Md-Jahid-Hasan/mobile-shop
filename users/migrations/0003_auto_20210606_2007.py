# Generated by Django 3.1.7 on 2021-06-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210301_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='is_empty',
            field=models.BooleanField(default=False),
        ),
    ]
