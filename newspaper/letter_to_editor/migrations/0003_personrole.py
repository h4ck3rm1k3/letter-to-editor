# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_to_editor', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonRole',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=50)),
                ('person', models.ForeignKey(to='letter_to_editor.Person', to_field=u'id')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
