# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_comment_original_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='original_post',
            new_name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=75, default='temp@temp.dk'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=42),
            preserve_default=True,
        ),
    ]
