# Generated by Django 2.1.7 on 2019-07-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcje', '0007_auto_20190720_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('wielkopsy', 'wielkopsy'), ('maluchy', 'maluchy'), ('czarnulki', 'czarnulki'), ('białaski', 'białaski'), ('rudzielce', 'rudzielce'), ('łaciate krówki', 'łaciate krówki'), ('kłapouszki', 'kłapouszki')], max_length=64),
        ),
    ]
