# Generated by Django 2.2 on 2019-04-14 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='yelp_id',
        ),
    ]
