# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_promotor_promotor_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotor',
            options={'ordering': ['user'], 'permissions': (('puede_ser_promotor', 'puede_ser_promotor'),)},
        ),
        migrations.AlterModelOptions(
            name='promovido',
            options={},
        ),
        migrations.AlterField(
            model_name='promovido',
            name='promovido_nombre',
            field=models.CharField(max_length=64),
        ),
    ]
