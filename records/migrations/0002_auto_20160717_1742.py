# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='visit',
            name='visit_image',
        ),
        migrations.AddField(
            model_name='image',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Visit'),
        ),
    ]
