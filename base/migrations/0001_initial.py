# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-10 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bimbingan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('hasil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sidang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=14)),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('nidn', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            bases=('base.user',),
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('npm', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('akun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.User')),
            ],
            bases=('base.user',),
        ),
        migrations.AddField(
            model_name='sidang',
            name='mhs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='dosen',
            name='akun',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.User'),
        ),
    ]