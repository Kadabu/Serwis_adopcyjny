# Generated by Django 2.1.7 on 2019-07-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0014_auto_20190722_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='picture',
            new_name='picture_1',
        ),
        migrations.AddField(
            model_name='dog',
            name='picture_2',
            field=models.ImageField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='dog',
            name='picture_3',
            field=models.ImageField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='dog',
            name='picture_4',
            field=models.ImageField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='dog',
            name='picture_5',
            field=models.ImageField(default=None, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='dog',
            name='picture_6',
            field=models.ImageField(default=None, null=True, upload_to='documents/'),
        ),
    ]