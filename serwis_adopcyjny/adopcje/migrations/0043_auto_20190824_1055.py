# Generated by Django 2.2.4 on 2019-08-24 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0042_auto_20190823_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='picture_2',
            new_name='picture',
        ),
    ]