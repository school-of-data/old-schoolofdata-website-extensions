# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'TopicTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_topic_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_tag_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SkillTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_skill_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'AudienceTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_audience_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ToolTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_tool_translation', ['language_code', 'master_id'])

        # Deleting model 'Topic'
        db.delete_table(u'courses_topic')

        # Deleting model 'ToolTranslation'
        db.delete_table(u'courses_tool_translation')

        # Deleting model 'AudienceTranslation'
        db.delete_table(u'courses_audience_translation')

        # Deleting model 'Audience'
        db.delete_table(u'courses_audience')

        # Deleting model 'SkillTranslation'
        db.delete_table(u'courses_skill_translation')

        # Deleting model 'Skill'
        db.delete_table(u'courses_skill')

        # Deleting model 'Tool'
        db.delete_table(u'courses_tool')

        # Deleting model 'TagTranslation'
        db.delete_table(u'courses_tag_translation')

        # Deleting model 'TopicTranslation'
        db.delete_table(u'courses_topic_translation')

        # Deleting model 'Tag'
        db.delete_table(u'courses_tag')


        # Changing field 'ModuleTranslation.description'
        db.alter_column(u'courses_module_translation', 'description', self.gf('django.db.models.fields.TextField')(max_length=2000))
        # Removing M2M table for field tool on 'Module'
        db.delete_table(db.shorten_name(u'courses_module_tool'))

        # Removing M2M table for field topic on 'Module'
        db.delete_table(db.shorten_name(u'courses_module_topic'))

        # Removing M2M table for field tag on 'Module'
        db.delete_table(db.shorten_name(u'courses_module_tag'))

        # Removing M2M table for field skill on 'Module'
        db.delete_table(db.shorten_name(u'courses_module_skill'))

        # Removing M2M table for field audience on 'Module'
        db.delete_table(db.shorten_name(u'courses_module_audience'))


    def backwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'courses_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'courses', ['Topic'])

        # Adding model 'ToolTranslation'
        db.create_table(u'courses_tool_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Tool'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'courses', ['ToolTranslation'])

        # Adding unique constraint on 'ToolTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_tool_translation', ['language_code', 'master_id'])

        # Adding model 'AudienceTranslation'
        db.create_table(u'courses_audience_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Audience'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'courses', ['AudienceTranslation'])

        # Adding unique constraint on 'AudienceTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_audience_translation', ['language_code', 'master_id'])

        # Adding model 'Audience'
        db.create_table(u'courses_audience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal(u'courses', ['Audience'])

        # Adding model 'SkillTranslation'
        db.create_table(u'courses_skill_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Skill'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'courses', ['SkillTranslation'])

        # Adding unique constraint on 'SkillTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_skill_translation', ['language_code', 'master_id'])

        # Adding model 'Skill'
        db.create_table(u'courses_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal(u'courses', ['Skill'])

        # Adding model 'Tool'
        db.create_table(u'courses_tool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal(u'courses', ['Tool'])

        # Adding model 'TagTranslation'
        db.create_table(u'courses_tag_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Tag'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'courses', ['TagTranslation'])

        # Adding unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_tag_translation', ['language_code', 'master_id'])

        # Adding model 'TopicTranslation'
        db.create_table(u'courses_topic_translation', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Topic'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'courses', ['TopicTranslation'])

        # Adding unique constraint on 'TopicTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_topic_translation', ['language_code', 'master_id'])

        # Adding model 'Tag'
        db.create_table(u'courses_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal(u'courses', ['Tag'])


        # Changing field 'ModuleTranslation.description'
        db.alter_column(u'courses_module_translation', 'description', self.gf('django.db.models.fields.TextField')())
        # Adding M2M table for field tool on 'Module'
        m2m_table_name = db.shorten_name(u'courses_module_tool')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm[u'courses.module'], null=False)),
            ('tool', models.ForeignKey(orm[u'courses.tool'], null=False))
        ))
        db.create_unique(m2m_table_name, ['module_id', 'tool_id'])

        # Adding M2M table for field topic on 'Module'
        m2m_table_name = db.shorten_name(u'courses_module_topic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm[u'courses.module'], null=False)),
            ('topic', models.ForeignKey(orm[u'courses.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['module_id', 'topic_id'])

        # Adding M2M table for field tag on 'Module'
        m2m_table_name = db.shorten_name(u'courses_module_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm[u'courses.module'], null=False)),
            ('tag', models.ForeignKey(orm[u'courses.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['module_id', 'tag_id'])

        # Adding M2M table for field skill on 'Module'
        m2m_table_name = db.shorten_name(u'courses_module_skill')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm[u'courses.module'], null=False)),
            ('skill', models.ForeignKey(orm[u'courses.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['module_id', 'skill_id'])

        # Adding M2M table for field audience on 'Module'
        m2m_table_name = db.shorten_name(u'courses_module_audience')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('module', models.ForeignKey(orm[u'courses.module'], null=False)),
            ('audience', models.ForeignKey(orm[u'courses.audience'], null=False))
        ))
        db.create_unique(m2m_table_name, ['module_id', 'audience_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'badgeclient.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.coursemodule': {
            'Meta': {'object_name': 'CourseModule'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Module']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'courses.coursetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CourseTranslation', 'db_table': "u'courses_course_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Course']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'courses.module': {
            'Meta': {'object_name': 'Module'},
            'completedby': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'completed'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'contributor': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contributed'", 'to': u"orm['auth.User']", 'db_table': "'models_contribution'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.Quiz']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.moduletranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ModuleTranslation', 'db_table': "u'courses_module_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Module']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'simplequiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'badge': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'badge_service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['badgeclient.BadgeService']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_right': ('django.db.models.fields.IntegerField', [], {'default': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['courses']