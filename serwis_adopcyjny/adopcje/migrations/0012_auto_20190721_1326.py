# Generated by Django 2.1.7 on 2019-07-21 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0011_auto_20190721_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='concerns',
            new_name='dog',
        ),
    ]
