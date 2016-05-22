# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promotor_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('no_promovidos', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'permissions': (('puede_ser_promotor', 'Puede ser promotor'),),
            },
        ),
        migrations.CreateModel(
            name='Promovido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promovido_id', models.IntegerField()),
                ('promovido_nombre', models.CharField(max_length=130)),
                ('voto', models.NullBooleanField()),
                ('promotor', models.ForeignKey(to='home.Promotor')),
            ],
            options={
                'permissions': (('puede_ser_promovido', 'Puede ser promovido'),),
            },
        ),
    ]
