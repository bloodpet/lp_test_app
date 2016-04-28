# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unsubscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnsubscribeSurvey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255)),
                ('reason', models.CharField(max_length=32, choices=[(b'STOP', b'I no longer want to receive these emails'), (b'NOSIGNUP', b'I never signed up for this mailing list'), (b'INAPPROPRIATE', b'The emails are inappropriate'), (b'SPAM', b'The emails are spam and should be reported'), (b'OTHER', b'Other')])),
                ('is_other', models.BooleanField(default=False)),
                ('other_reason', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnsubscribeSurveyCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=32, choices=[(b'STOP', b'I no longer want to receive these emails'), (b'NOSIGNUP', b'I never signed up for this mailing list'), (b'INAPPROPRIATE', b'The emails are inappropriate'), (b'SPAM', b'The emails are spam and should be reported'), (b'OTHER', b'Other')])),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
