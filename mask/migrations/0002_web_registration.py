# Generated by Django 3.0.5 on 2020-05-03 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('shop_owner', models.CharField(max_length=255)),
                ('mask_avail', models.CharField(max_length=255)),
                ('mask_price', models.CharField(max_length=255)),
                ('sanitizer_avail', models.CharField(max_length=255)),
                ('sanitizer_price', models.CharField(max_length=255)),
                ('shop_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('update_date', models.DateField(default=datetime.date.today)),
                ('update_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
