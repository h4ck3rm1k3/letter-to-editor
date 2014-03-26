# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('ar_id', models.IntegerField(serialize=False, primary_key=True)),
                ('ar_namespace', models.IntegerField()),
                ('ar_title', models.CharField(max_length=255)),
                ('ar_text', models.TextField()),
                ('ar_comment', models.TextField()),
                ('ar_user', models.IntegerField()),
                ('ar_user_text', models.CharField(max_length=255)),
                ('ar_timestamp', models.CharField(max_length=14)),
                ('ar_minor_edit', models.IntegerField()),
                ('ar_flags', models.TextField()),
                ('ar_rev_id', models.IntegerField(null=True, blank=True)),
                ('ar_text_id', models.IntegerField(null=True, blank=True)),
                ('ar_deleted', models.IntegerField()),
                ('ar_len', models.IntegerField(null=True, blank=True)),
                ('ar_page_id', models.IntegerField(null=True, blank=True)),
                ('ar_parent_id', models.IntegerField(null=True, blank=True)),
                ('ar_sha1', models.CharField(max_length=32)),
                ('ar_content_model', models.CharField(max_length=32, blank=True)),
                ('ar_content_format', models.CharField(max_length=64, blank=True)),
            ],
            options={
                u'db_table': u'archive',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Externallinks',
            fields=[
                ('el_id', models.IntegerField(serialize=False, primary_key=True)),
                ('el_from', models.IntegerField()),
                ('el_to', models.TextField()),
                ('el_index', models.TextField()),
            ],
            options={
                u'db_table': u'externallinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteIdentifiers',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_site', models.IntegerField()),
                ('si_type', models.CharField(max_length=32)),
                ('si_key', models.CharField(max_length=32)),
            ],
            options={
                u'db_table': u'site_identifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='L10NCache',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('lc_lang', models.CharField(max_length=32)),
                ('lc_key', models.CharField(max_length=255)),
                ('lc_value', models.TextField()),
            ],
            options={
                u'db_table': u'l10n_cache',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProtectedTitles',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('pt_namespace', models.IntegerField()),
                ('pt_title', models.CharField(max_length=255)),
                ('pt_user', models.IntegerField()),
                ('pt_reason', models.TextField(blank=True)),
                ('pt_timestamp', models.CharField(max_length=14)),
                ('pt_expiry', models.CharField(max_length=14)),
                ('pt_create_perm', models.CharField(max_length=60)),
            ],
            options={
                u'db_table': u'protected_titles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.IntegerField(serialize=False, primary_key=True)),
                ('job_cmd', models.CharField(max_length=60)),
                ('job_namespace', models.IntegerField()),
                ('job_title', models.CharField(max_length=255)),
                ('job_timestamp', models.CharField(max_length=14, blank=True)),
                ('job_params', models.TextField()),
                ('job_random', models.IntegerField()),
                ('job_attempts', models.IntegerField()),
                ('job_token', models.CharField(max_length=32)),
                ('job_token_timestamp', models.CharField(max_length=14, blank=True)),
                ('job_sha1', models.CharField(max_length=32)),
            ],
            options={
                u'db_table': u'job',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Langlinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ll_from', models.IntegerField()),
                ('ll_lang', models.CharField(max_length=20)),
                ('ll_title', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'langlinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageProps',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('pp_page', models.IntegerField()),
                ('pp_propname', models.CharField(max_length=60)),
                ('pp_value', models.TextField()),
            ],
            options={
                u'db_table': u'page_props',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogSearch',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ls_field', models.CharField(max_length=32)),
                ('ls_value', models.CharField(max_length=255)),
                ('ls_log_id', models.IntegerField()),
            ],
            options={
                u'db_table': u'log_search',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Iwlinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('iwl_from', models.IntegerField()),
                ('iwl_prefix', models.CharField(max_length=20)),
                ('iwl_title', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'iwlinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MsgResource',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('mr_resource', models.CharField(max_length=255)),
                ('mr_lang', models.CharField(max_length=32)),
                ('mr_blob', models.TextField()),
                ('mr_timestamp', models.CharField(max_length=14)),
            ],
            options={
                u'db_table': u'msg_resource',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hitcounter',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('hc_id', models.IntegerField()),
            ],
            options={
                u'db_table': u'hitcounter',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuerycacheInfo',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('qci_type', models.CharField(unique=True, max_length=32)),
                ('qci_timestamp', models.CharField(max_length=14)),
            ],
            options={
                u'db_table': u'querycache_info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('rev_id', models.IntegerField(serialize=False, primary_key=True)),
                ('rev_page', models.IntegerField()),
                ('rev_text_id', models.IntegerField()),
                ('rev_comment', models.TextField()),
                ('rev_user', models.IntegerField()),
                ('rev_user_text', models.CharField(max_length=255)),
                ('rev_timestamp', models.CharField(max_length=14)),
                ('rev_minor_edit', models.IntegerField()),
                ('rev_deleted', models.IntegerField()),
                ('rev_len', models.IntegerField(null=True, blank=True)),
                ('rev_parent_id', models.IntegerField(null=True, blank=True)),
                ('rev_sha1', models.CharField(max_length=32)),
                ('rev_content_model', models.CharField(max_length=32, blank=True)),
                ('rev_content_format', models.CharField(max_length=64, blank=True)),
            ],
            options={
                u'db_table': u'revision',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagelinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('pl_from', models.IntegerField()),
                ('pl_namespace', models.IntegerField()),
                ('pl_title', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'pagelinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Searchindex',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('si_page', models.IntegerField(unique=True)),
                ('si_title', models.CharField(max_length=255)),
                ('si_text', models.TextField()),
            ],
            options={
                u'db_table': u'searchindex',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Updatelog',
            fields=[
                ('ul_key', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('ul_value', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'updatelog',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Querycachetwo',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('qcc_type', models.CharField(max_length=32)),
                ('qcc_value', models.IntegerField()),
                ('qcc_namespace', models.IntegerField()),
                ('qcc_title', models.CharField(max_length=255)),
                ('qcc_namespacetwo', models.IntegerField()),
                ('qcc_titletwo', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'querycachetwo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Templatelinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('tl_from', models.IntegerField()),
                ('tl_namespace', models.IntegerField()),
                ('tl_title', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'templatelinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('site_id', models.IntegerField(serialize=False, primary_key=True)),
                ('site_global_key', models.CharField(unique=True, max_length=32)),
                ('site_type', models.CharField(max_length=32)),
                ('site_group', models.CharField(max_length=32)),
                ('site_source', models.CharField(max_length=32)),
                ('site_language', models.CharField(max_length=32)),
                ('site_protocol', models.CharField(max_length=32)),
                ('site_domain', models.CharField(max_length=255)),
                ('site_data', models.TextField()),
                ('site_forward', models.IntegerField()),
                ('site_config', models.TextField()),
            ],
            options={
                u'db_table': u'sites',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProperties',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('up_user', models.IntegerField()),
                ('up_property', models.CharField(max_length=255)),
                ('up_value', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'user_properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagSummary',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ts_rc_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('ts_log_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('ts_rev_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('ts_tags', models.TextField()),
            ],
            options={
                u'db_table': u'tag_summary',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oldimage',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('oi_name', models.CharField(max_length=255)),
                ('oi_archive_name', models.CharField(max_length=255)),
                ('oi_size', models.IntegerField()),
                ('oi_width', models.IntegerField()),
                ('oi_height', models.IntegerField()),
                ('oi_bits', models.IntegerField()),
                ('oi_description', models.TextField()),
                ('oi_user', models.IntegerField()),
                ('oi_user_text', models.CharField(max_length=255)),
                ('oi_timestamp', models.CharField(max_length=14)),
                ('oi_metadata', models.TextField()),
                ('oi_media_type', models.CharField(max_length=10, blank=True)),
                ('oi_major_mime', models.CharField(max_length=11)),
                ('oi_minor_mime', models.CharField(max_length=100)),
                ('oi_deleted', models.IntegerField()),
                ('oi_sha1', models.CharField(max_length=32)),
            ],
            options={
                u'db_table': u'oldimage',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageRestrictions',
            fields=[
                ('pr_id', models.IntegerField(serialize=False, primary_key=True)),
                ('pr_page', models.IntegerField()),
                ('pr_type', models.CharField(max_length=60)),
                ('pr_level', models.CharField(max_length=60)),
                ('pr_cascade', models.IntegerField()),
                ('pr_user', models.IntegerField(null=True, blank=True)),
                ('pr_expiry', models.CharField(max_length=14, blank=True)),
            ],
            options={
                u'db_table': u'page_restrictions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filearchive',
            fields=[
                ('fa_id', models.IntegerField(serialize=False, primary_key=True)),
                ('fa_name', models.CharField(max_length=255)),
                ('fa_archive_name', models.CharField(max_length=255, blank=True)),
                ('fa_storage_group', models.CharField(max_length=16, blank=True)),
                ('fa_storage_key', models.CharField(max_length=64, blank=True)),
                ('fa_deleted_user', models.IntegerField(null=True, blank=True)),
                ('fa_deleted_timestamp', models.CharField(max_length=14, blank=True)),
                ('fa_deleted_reason', models.TextField(blank=True)),
                ('fa_size', models.IntegerField(null=True, blank=True)),
                ('fa_width', models.IntegerField(null=True, blank=True)),
                ('fa_height', models.IntegerField(null=True, blank=True)),
                ('fa_metadata', models.TextField(blank=True)),
                ('fa_bits', models.IntegerField(null=True, blank=True)),
                ('fa_media_type', models.CharField(max_length=10, blank=True)),
                ('fa_major_mime', models.CharField(max_length=11, blank=True)),
                ('fa_minor_mime', models.CharField(max_length=100, blank=True)),
                ('fa_description', models.TextField(blank=True)),
                ('fa_user', models.IntegerField(null=True, blank=True)),
                ('fa_user_text', models.CharField(max_length=255, blank=True)),
                ('fa_timestamp', models.CharField(max_length=14, blank=True)),
                ('fa_deleted', models.IntegerField()),
                ('fa_sha1', models.CharField(max_length=32)),
            ],
            options={
                u'db_table': u'filearchive',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('img_size', models.IntegerField()),
                ('img_width', models.IntegerField()),
                ('img_height', models.IntegerField()),
                ('img_metadata', models.TextField()),
                ('img_bits', models.IntegerField()),
                ('img_media_type', models.CharField(max_length=10, blank=True)),
                ('img_major_mime', models.CharField(max_length=11)),
                ('img_minor_mime', models.CharField(max_length=100)),
                ('img_description', models.TextField()),
                ('img_user', models.IntegerField()),
                ('img_user_text', models.CharField(max_length=255)),
                ('img_timestamp', models.CharField(max_length=14)),
                ('img_sha1', models.CharField(max_length=32)),
            ],
            options={
                u'db_table': u'image',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserNewtalk',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('user_ip', models.CharField(max_length=40)),
                ('user_last_timestamp', models.CharField(max_length=14, blank=True)),
            ],
            options={
                u'db_table': u'user_newtalk',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interwiki',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('iw_prefix', models.CharField(unique=True, max_length=32)),
                ('iw_url', models.TextField()),
                ('iw_api', models.TextField()),
                ('iw_wikiid', models.CharField(max_length=64)),
                ('iw_local', models.IntegerField()),
                ('iw_trans', models.IntegerField()),
            ],
            options={
                u'db_table': u'interwiki',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Objectcache',
            fields=[
                ('keyname', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('value', models.TextField(blank=True)),
                ('exptime', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'objectcache',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('wl_user', models.IntegerField()),
                ('wl_namespace', models.IntegerField()),
                ('wl_title', models.CharField(max_length=255)),
                ('wl_notificationtimestamp', models.CharField(max_length=14, blank=True)),
            ],
            options={
                u'db_table': u'watchlist',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.IntegerField(serialize=False, primary_key=True)),
                ('cat_title', models.CharField(unique=True, max_length=255)),
                ('cat_pages', models.IntegerField()),
                ('cat_subcats', models.IntegerField()),
                ('cat_files', models.IntegerField()),
            ],
            options={
                u'db_table': u'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValidTag',
            fields=[
                ('vt_tag', models.CharField(max_length=255, serialize=False, primary_key=True)),
            ],
            options={
                u'db_table': u'valid_tag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transcache',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('tc_url', models.CharField(unique=True, max_length=255)),
                ('tc_contents', models.TextField(blank=True)),
                ('tc_time', models.CharField(max_length=14)),
            ],
            options={
                u'db_table': u'transcache',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.IntegerField(serialize=False, primary_key=True)),
                ('page_namespace', models.IntegerField()),
                ('page_title', models.CharField(max_length=255)),
                ('page_restrictions', models.TextField()),
                ('page_counter', models.BigIntegerField()),
                ('page_is_redirect', models.IntegerField()),
                ('page_is_new', models.IntegerField()),
                ('page_random', models.FloatField()),
                ('page_touched', models.CharField(max_length=14)),
                ('page_links_updated', models.CharField(max_length=14, blank=True)),
                ('page_latest', models.IntegerField()),
                ('page_len', models.IntegerField()),
                ('page_content_model', models.CharField(max_length=32, blank=True)),
            ],
            options={
                u'db_table': u'page',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imagelinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('il_from', models.IntegerField()),
                ('il_to', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'imagelinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('old_id', models.IntegerField(serialize=False, primary_key=True)),
                ('old_text', models.TextField()),
                ('old_flags', models.TextField()),
            ],
            options={
                u'db_table': u'text',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Querycache',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('qc_type', models.CharField(max_length=32)),
                ('qc_value', models.IntegerField()),
                ('qc_namespace', models.IntegerField()),
                ('qc_title', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'querycache',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteStats',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ss_row_id', models.IntegerField(unique=True)),
                ('ss_total_views', models.BigIntegerField(null=True, blank=True)),
                ('ss_total_edits', models.BigIntegerField(null=True, blank=True)),
                ('ss_good_articles', models.BigIntegerField(null=True, blank=True)),
                ('ss_total_pages', models.BigIntegerField(null=True, blank=True)),
                ('ss_users', models.BigIntegerField(null=True, blank=True)),
                ('ss_active_users', models.BigIntegerField(null=True, blank=True)),
                ('ss_images', models.IntegerField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'site_stats',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recentchanges',
            fields=[
                ('rc_id', models.IntegerField(serialize=False, primary_key=True)),
                ('rc_timestamp', models.CharField(max_length=14)),
                ('rc_cur_time', models.CharField(max_length=14)),
                ('rc_user', models.IntegerField()),
                ('rc_user_text', models.CharField(max_length=255)),
                ('rc_namespace', models.IntegerField()),
                ('rc_title', models.CharField(max_length=255)),
                ('rc_comment', models.CharField(max_length=255)),
                ('rc_minor', models.IntegerField()),
                ('rc_bot', models.IntegerField()),
                ('rc_new', models.IntegerField()),
                ('rc_cur_id', models.IntegerField()),
                ('rc_this_oldid', models.IntegerField()),
                ('rc_last_oldid', models.IntegerField()),
                ('rc_type', models.IntegerField()),
                ('rc_source', models.CharField(max_length=16)),
                ('rc_patrolled', models.IntegerField()),
                ('rc_ip', models.CharField(max_length=40)),
                ('rc_old_len', models.IntegerField(null=True, blank=True)),
                ('rc_new_len', models.IntegerField(null=True, blank=True)),
                ('rc_deleted', models.IntegerField()),
                ('rc_logid', models.IntegerField()),
                ('rc_log_type', models.CharField(max_length=255, blank=True)),
                ('rc_log_action', models.CharField(max_length=255, blank=True)),
                ('rc_params', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'recentchanges',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Uploadstash',
            fields=[
                ('us_id', models.IntegerField(serialize=False, primary_key=True)),
                ('us_user', models.IntegerField()),
                ('us_key', models.CharField(unique=True, max_length=255)),
                ('us_orig_path', models.CharField(max_length=255)),
                ('us_path', models.CharField(max_length=255)),
                ('us_source_type', models.CharField(max_length=50, blank=True)),
                ('us_timestamp', models.CharField(max_length=14)),
                ('us_status', models.CharField(max_length=50)),
                ('us_chunk_inx', models.IntegerField(null=True, blank=True)),
                ('us_props', models.TextField(blank=True)),
                ('us_size', models.IntegerField()),
                ('us_sha1', models.CharField(max_length=31)),
                ('us_mime', models.CharField(max_length=255, blank=True)),
                ('us_media_type', models.CharField(max_length=10, blank=True)),
                ('us_image_width', models.IntegerField(null=True, blank=True)),
                ('us_image_height', models.IntegerField(null=True, blank=True)),
                ('us_image_bits', models.IntegerField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'uploadstash',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('rd_from', models.IntegerField(serialize=False, primary_key=True)),
                ('rd_namespace', models.IntegerField()),
                ('rd_title', models.CharField(max_length=255)),
                ('rd_interwiki', models.CharField(max_length=32, blank=True)),
                ('rd_fragment', models.CharField(max_length=255, blank=True)),
            ],
            options={
                u'db_table': u'redirect',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ug_user', models.IntegerField()),
                ('ug_group', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'user_groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categorylinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('cl_from', models.IntegerField()),
                ('cl_to', models.CharField(max_length=255)),
                ('cl_sortkey', models.CharField(max_length=230)),
                ('cl_sortkey_prefix', models.CharField(max_length=255)),
                ('cl_timestamp', models.DateTimeField()),
                ('cl_collation', models.CharField(max_length=32)),
                ('cl_type', models.CharField(max_length=6)),
            ],
            options={
                u'db_table': u'categorylinks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=255)),
                ('user_real_name', models.CharField(max_length=255)),
                ('user_password', models.TextField()),
                ('user_newpassword', models.TextField()),
                ('user_newpass_time', models.CharField(max_length=14, blank=True)),
                ('user_email', models.TextField()),
                ('user_touched', models.CharField(max_length=14)),
                ('user_token', models.CharField(max_length=32)),
                ('user_email_authenticated', models.CharField(max_length=14, blank=True)),
                ('user_email_token', models.CharField(max_length=32, blank=True)),
                ('user_email_token_expires', models.CharField(max_length=14, blank=True)),
                ('user_registration', models.CharField(max_length=14, blank=True)),
                ('user_editcount', models.IntegerField(null=True, blank=True)),
                ('user_password_expires', models.CharField(max_length=14, blank=True)),
            ],
            options={
                u'db_table': u'user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ipblocks',
            fields=[
                ('ipb_id', models.IntegerField(serialize=False, primary_key=True)),
                ('ipb_address', models.TextField()),
                ('ipb_user', models.IntegerField()),
                ('ipb_by', models.IntegerField()),
                ('ipb_by_text', models.CharField(max_length=255)),
                ('ipb_reason', models.TextField()),
                ('ipb_timestamp', models.CharField(max_length=14)),
                ('ipb_auto', models.IntegerField()),
                ('ipb_anon_only', models.IntegerField()),
                ('ipb_create_account', models.IntegerField()),
                ('ipb_enable_autoblock', models.IntegerField()),
                ('ipb_expiry', models.CharField(max_length=14)),
                ('ipb_range_start', models.TextField()),
                ('ipb_range_end', models.TextField()),
                ('ipb_deleted', models.IntegerField()),
                ('ipb_block_email', models.IntegerField()),
                ('ipb_allow_usertalk', models.IntegerField()),
                ('ipb_parent_block_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'ipblocks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MsgResourceLinks',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('mrl_resource', models.CharField(max_length=255)),
                ('mrl_message', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'msg_resource_links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleDeps',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('md_module', models.CharField(max_length=255)),
                ('md_skin', models.CharField(max_length=32)),
                ('md_deps', models.TextField()),
            ],
            options={
                u'db_table': u'module_deps',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFormerGroups',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ufg_user', models.IntegerField()),
                ('ufg_group', models.CharField(max_length=255)),
            ],
            options={
                u'db_table': u'user_former_groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChangeTag',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('ct_rc_id', models.IntegerField(null=True, blank=True)),
                ('ct_log_id', models.IntegerField(null=True, blank=True)),
                ('ct_rev_id', models.IntegerField(null=True, blank=True)),
                ('ct_tag', models.CharField(max_length=255)),
                ('ct_params', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'change_tag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logging',
            fields=[
                ('log_id', models.IntegerField(serialize=False, primary_key=True)),
                ('log_type', models.CharField(max_length=32)),
                ('log_action', models.CharField(max_length=32)),
                ('log_timestamp', models.CharField(max_length=14)),
                ('log_user', models.IntegerField()),
                ('log_user_text', models.CharField(max_length=255)),
                ('log_namespace', models.IntegerField()),
                ('log_title', models.CharField(max_length=255)),
                ('log_page', models.IntegerField(null=True, blank=True)),
                ('log_comment', models.CharField(max_length=255)),
                ('log_params', models.TextField()),
                ('log_deleted', models.IntegerField()),
            ],
            options={
                u'db_table': u'logging',
            },
            bases=(models.Model,),
        ),
    ]
