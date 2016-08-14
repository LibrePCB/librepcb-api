# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('dependencies', models.ManyToManyField(blank=True, to='api.Library', related_name='_library_dependencies_+')),
            ],
            options={
                'verbose_name_plural': 'libraries',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='publisher',
            field=models.ForeignKey(to='api.Publisher'),
        ),
    ]
