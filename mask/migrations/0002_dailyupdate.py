# Generated by Django 3.0.5 on 2020-04-27 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(max_length=255)),
                ('shop_open', models.CharField(max_length=10)),
                ('mask_avail', models.CharField(max_length=10)),
                ('sanitizer_avail', models.CharField(max_length=10)),
                ('update_date', models.DateField(default=datetime.date.today)),
                ('update_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
