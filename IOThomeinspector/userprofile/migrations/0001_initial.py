# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices', multiselectfield.db.fields.MultiSelectField(choices=[('philips-hue', 'Philips Hue'), ('amazon-echoe', 'Amazon Echoe'), ('nest', 'Nest'), ('fitbit', 'FitBit')], max_length=36)),
                ('userprofile_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
    ]