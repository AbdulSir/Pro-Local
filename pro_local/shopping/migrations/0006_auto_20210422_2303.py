# Generated by Django 3.1.5 on 2021-04-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20210422_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_keys',
            field=models.CharField(max_length=160),
        ),
    ]