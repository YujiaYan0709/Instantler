# Generated by Django 2.2 on 2019-04-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0005_auto_20190418_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastorderreview',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]
