# Generated by Django 2.1.7 on 2019-07-14 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0004_auto_20190714_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dodany',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='dog',
            name='opis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
