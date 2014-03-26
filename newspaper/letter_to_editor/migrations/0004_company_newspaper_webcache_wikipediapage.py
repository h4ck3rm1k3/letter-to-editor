# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_to_editor', '0003_personrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ForeignKey(to='letter_to_editor.Image', to_field=u'id')),
                ('image', models.ForeignKey(to='letter_to_editor.Image', to_field=u'id')),
                ('headquarters', models.ForeignKey(to='letter_to_editor.Location', to_field=u'id')),
                ('website', models.ForeignKey(to='letter_to_editor.Website', to_field='url')),
                ('foundation', models.DateField()),
                ('owners', models.ManyToManyField(to='letter_to_editor.Person')),
                ('staff', models.ManyToManyField(to='letter_to_editor.PersonRole')),
                ('phone', models.ManyToManyField(to='letter_to_editor.Phone')),
                ('history', models.ManyToManyField(to='letter_to_editor.History')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Webcache',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('page', models.ForeignKey(to='letter_to_editor.Webpage', to_field='url')),
                ('contents', models.FileField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WikipediaPage',
            fields=[
                (u'webpage_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='url', serialize=False, to='letter_to_editor.Webpage')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('letter_to_editor.webpage',),
        ),
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                (u'company_ptr', models.OneToOneField(auto_created=True, to_field=u'id', to='letter_to_editor.Company')),
                ('newspaper_name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('newspaper_type', models.CharField(max_length=50)),
                ('newspaper_format', models.CharField(max_length=50)),
                ('dirinteractive', models.ForeignKey(to='letter_to_editor.PersonRole', to_field=u'id')),
                ('political', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('ceased_publication', models.DateField()),
                ('ISSN', models.CharField(max_length=50)),
                ('oclc', models.CharField(max_length=50)),
                ('free', models.ForeignKey(to='letter_to_editor.Website', to_field='url')),
                ('circulation', models.ManyToManyField(to='letter_to_editor.CirculationHistory')),
            ],
            options={
            },
            bases=('letter_to_editor.company',),
        ),
    ]
