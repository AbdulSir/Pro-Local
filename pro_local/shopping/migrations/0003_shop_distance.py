# Generated by Django 3.1.5 on 2021-04-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20210422_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='distance',
            field=models.CharField(default='0 KM', max_length=20),
        ),
    ]
