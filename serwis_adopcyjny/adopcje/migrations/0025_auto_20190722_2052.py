# Generated by Django 2.2.3 on 2019-07-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0024_auto_20190722_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture_6',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
