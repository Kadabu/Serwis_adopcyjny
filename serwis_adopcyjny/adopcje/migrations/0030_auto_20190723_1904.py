# Generated by Django 2.2.3 on 2019-07-23 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0029_auto_20190723_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptionform',
            old_name='prev_dog',
            new_name='prev_dogs',
        ),
    ]
