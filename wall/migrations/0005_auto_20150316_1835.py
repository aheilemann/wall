# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wall', '0004_auto_20150226_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ban_reason', models.TextField()),
                ('banned_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='wall.Post', related_name='comments'),
            preserve_default=True,
        ),
    ]
