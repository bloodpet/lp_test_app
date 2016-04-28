# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unsubscribe', '0002_unsubscribesurvey_unsubscribesurveycount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unsubscribesurvey',
            name='other_reason',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
