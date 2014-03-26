# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_to_editor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('social', models.ManyToManyField(to='letter_to_editor.SocialAccount')),
                ('phone', models.ManyToManyField(to='letter_to_editor.Phone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
