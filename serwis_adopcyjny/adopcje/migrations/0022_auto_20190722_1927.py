# Generated by Django 2.2.3 on 2019-07-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0021_dog_contact_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture_2',
            field=models.ImageField(null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='picture_3',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='picture_4',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]
