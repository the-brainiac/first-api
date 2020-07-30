# Generated by Django 3.0.8 on 2020-07-29 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('pin_code', models.CharField(max_length=6, unique=True, verbose_name='Pin Code')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.State')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.Town')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
                ('pin_code', models.CharField(max_length=6, unique=True, verbose_name='Pin Code')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.Country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.State')),
            ],
        ),
    ]