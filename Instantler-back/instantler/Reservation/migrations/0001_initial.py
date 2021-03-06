# Generated by Django 2.2 on 2019-04-13 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Table', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestNum', models.IntegerField(default=1)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Restaurant')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Table.TableType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PastOrderReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
