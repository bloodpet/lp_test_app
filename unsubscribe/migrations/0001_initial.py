# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import unsubscribe.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnsubscribeUrl',
            fields=[
                ('id', unsubscribe.fields.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, editable=False, primary_key=True)),
                ('email', models.EmailField(max_length=255)),
                ('sent_ts', models.DateTimeField(auto_now_add=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
