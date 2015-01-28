# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, verbose_name='id', primary_key=True)),
                ('novel', models.CharField(max_length=32, verbose_name='novel id', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u540d\u79f0', db_index=True)),
                ('pageid', models.BigIntegerField(unique=True, verbose_name='\u8d34\u5427id', db_index=True)),
                ('createtime', models.PositiveIntegerField(default=0, verbose_name='\u521b\u5efa\u65f6\u95f4', db_index=True)),
                ('updatetime', models.BigIntegerField(default=0, verbose_name='\u66f4\u65b0\u65f6\u95f4', db_index=True)),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u72b6\u6001', db_index=True)),
                ('content', models.TextField(default=b'', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'db_table': 'Chapter',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, verbose_name='id', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u540d\u79f0', db_index=True)),
                ('rule', models.CharField(default=b'.+', max_length=255, verbose_name='\u7ae0\u8282\u6807\u9898\u89c4\u5219')),
                ('createtime', models.PositiveIntegerField(default=0, verbose_name='\u521b\u5efa\u65f6\u95f4', db_index=True)),
                ('updatetime', models.PositiveIntegerField(default=0, verbose_name='\u66f4\u65b0\u65f6\u95f4', db_index=True)),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u72b6\u6001', db_index=True)),
            ],
            options={
                'db_table': 'Novel',
            },
            bases=(models.Model,),
        ),
    ]
