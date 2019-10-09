# Generated by Django 2.1.7 on 2019-07-21 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0010_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='to',
        ),
        migrations.AddField(
            model_name='message',
            name='concerns',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adopcje.Dog'),
            preserve_default=False,
        ),
    ]
