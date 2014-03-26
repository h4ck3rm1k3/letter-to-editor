# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('domain', models.CharField(max_length=255)),
                ('url', models.URLField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CirculationHistory',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('circulation', models.IntegerField(null=True, blank=True)),
                ('circulation_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('url', models.URLField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                (u'webpage_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='url', serialize=False, to='letter_to_editor.Webpage')),
                ('number', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=('letter_to_editor.webpage',),
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.ForeignKey(to='letter_to_editor.Website', to_field='url')),
                ('name', models.CharField(max_length=50)),
                ('page', models.ForeignKey(to='letter_to_editor.Webpage', to_field='url')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
