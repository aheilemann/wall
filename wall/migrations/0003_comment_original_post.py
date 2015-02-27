# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='original_post',
            field=models.ForeignKey(to='wall.Post', default=1),
            preserve_default=False,
        ),
    ]
