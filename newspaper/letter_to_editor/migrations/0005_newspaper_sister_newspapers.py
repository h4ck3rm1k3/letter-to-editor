# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_to_editor', '0004_company_newspaper_webcache_wikipediapage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='sister_newspapers',
            field=models.ForeignKey(to='letter_to_editor.Newspaper', to_field='newspaper_name'),
            preserve_default=True,
        ),
    ]
