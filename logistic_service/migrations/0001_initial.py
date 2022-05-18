# Generated by Django 4.0.4 on 2022-04-28 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('gn', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('manufacturer_model', models.CharField(max_length=80)),
                ('max_weight', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('phone_number', models.BigIntegerField()),
                ('state', models.CharField(max_length=45)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logistician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('lastname', models.CharField(max_length=80)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=45)),
                ('date', models.DateField(auto_now_add=True)),
                ('mass', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.BigIntegerField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.district')),
            ],
        ),
        migrations.CreateModel(
            name='Waybill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_waybill', models.IntegerField()),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('state', models.CharField(max_length=45)),
                ('distinct', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.district')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.driver')),
                ('logistician', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.logistician')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.order')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.district')),
            ],
        ),
    ]