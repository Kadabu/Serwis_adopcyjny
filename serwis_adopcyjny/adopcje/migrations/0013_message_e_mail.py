# Generated by Django 2.1.7 on 2019-07-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0012_auto_20190721_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='e_mail',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
