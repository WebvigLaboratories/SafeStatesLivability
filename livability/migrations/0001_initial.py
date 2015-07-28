# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment_Focus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selection', models.SmallIntegerField(choices=[(1, b'1-Development or Transportation Projects'), (2, b'2-Physical Environment of a Community, Neighborhood, or School'), (3, b'3-Policy, Plan, Codes, or Standards'), (4, b'4-Walkability, Bikability, and/or Transit Access')])),
            ],
            options={
                'ordering': ['toolname__name'],
            },
        ),
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selection', models.SmallIntegerField(choices=[(1, b'1-Elected Officials'), (2, b'2-Laypersons'), (3, b'3-Planners'), (4, b'4-PH Professionals'), (5, b'5-School Officials')])),
            ],
            options={
                'ordering': ['toolname__name'],
            },
        ),
        migrations.CreateModel(
            name='Community_Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selection', models.SmallIntegerField(choices=[(1, b'1-Urban'), (2, b'2-Rural')])),
            ],
            options={
                'ordering': ['toolname__name'],
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200, null=True, blank=True)),
                ('url', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('year_developed', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q_transportation', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('q_housing', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('q_investment', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('q_compact', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('q_health', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('q_preservation', models.SmallIntegerField(choices=[(0, b'No'), (1, b'Yes')])),
                ('toolname', models.OneToOneField(to='livability.Tools')),
            ],
            options={
                'ordering': ['toolname__name'],
            },
        ),
        migrations.AddField(
            model_name='community_size',
            name='toolname',
            field=models.ForeignKey(to='livability.Tools'),
        ),
        migrations.AddField(
            model_name='audience',
            name='toolname',
            field=models.ForeignKey(to='livability.Tools'),
        ),
        migrations.AddField(
            model_name='assessment_focus',
            name='toolname',
            field=models.ForeignKey(to='livability.Tools'),
        ),
    ]
