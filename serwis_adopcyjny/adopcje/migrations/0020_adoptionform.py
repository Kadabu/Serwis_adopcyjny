# Generated by Django 2.2.3 on 2019-07-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0019_auto_20190722_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_1', models.IntegerField(choices=[(1, 'tak'), (2, 'nie')])),
                ('field_2', models.IntegerField(choices=[(1, 'tak'), (2, 'nie')])),
                ('field_3', models.IntegerField(choices=[(1, 'w domu z ogrodem'), (2, 'w bloku/kamienicy'), (2, 'w innym miejscu')])),
                ('field_4', models.CharField(max_length=64)),
                ('field_5', models.CharField(blank=True, max_length=64, null=True)),
                ('field_6', models.IntegerField(blank=True, choices=[(1, 'tak'), (2, 'nie')], null=True)),
                ('field_7', models.IntegerField(choices=[(1, 'w domu/mieszkaniu'), (2, 'w domu/mieszkaniu w klatce kenelowej'), (3, 'w ogrodzie'), (4, 'w ogrodzie w kojcu')])),
                ('field_8', models.IntegerField()),
                ('field_9', models.IntegerField()),
                ('field_10', models.TextField()),
                ('field_11', models.CharField(max_length=128)),
                ('field_12', models.CharField(max_length=128)),
                ('field_13', models.TextField()),
                ('field_14', models.CharField(max_length=64)),
                ('field_15', models.EmailField(max_length=254)),
                ('field_16', models.CharField(max_length=32)),
                ('dog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcje.Dog')),
            ],
        ),
    ]