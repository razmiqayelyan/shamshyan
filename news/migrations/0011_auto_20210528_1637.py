# Generated by Django 3.1.7 on 2021-05-28 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210527_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 16, 37, 15, 194043)),
        ),
        migrations.AlterField(
            model_name='verificateuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 16, 37, 15, 209643)),
        ),
        migrations.AlterField(
            model_name='verificateuser',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]