# Generated by Django 2.2.4 on 2019-08-23 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0041_auto_20190820_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='picture_1',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_2',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_3',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_4',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_5',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_6',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_7',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='picture_8',
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopcje.Dog')),
            ],
        ),
    ]
