# Generated by Django 2.2 on 2019-04-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TakeANumber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitinguser',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
