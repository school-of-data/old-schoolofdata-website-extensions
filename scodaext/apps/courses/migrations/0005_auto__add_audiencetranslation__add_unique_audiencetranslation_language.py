# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AudienceTranslation'
        db.create_table(u'courses_audience_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Audience'])),
        ))
        db.send_create_signal(u'courses', ['AudienceTranslation'])

        # Adding unique constraint on 'AudienceTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_audience_translation', ['language_code', 'master_id'])

        # Adding model 'ToolTranslation'
        db.create_table(u'courses_tool_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Tool'])),
        ))
        db.send_create_signal(u'courses', ['ToolTranslation'])

        # Adding unique constraint on 'ToolTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_tool_translation', ['language_code', 'master_id'])

        # Adding model 'SkillTranslation'
        db.create_table(u'courses_skill_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Skill'])),
        ))
        db.send_create_signal(u'courses', ['SkillTranslation'])

        # Adding unique constraint on 'SkillTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_skill_translation', ['language_code', 'master_id'])

        # Adding model 'ModuleTranslation'
        db.create_table(u'courses_module_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Module'])),
        ))
        db.send_create_signal(u'courses', ['ModuleTranslation'])

        # Adding unique constraint on 'ModuleTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_module_translation', ['language_code', 'master_id'])

        # Adding model 'TopicTranslation'
        db.create_table(u'courses_topic_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Topic'])),
        ))
        db.send_create_signal(u'courses', ['TopicTranslation'])

        # Adding unique constraint on 'TopicTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_topic_translation', ['language_code', 'master_id'])

        # Adding model 'TagTranslation'
        db.create_table(u'courses_tag_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Tag'])),
        ))
        db.send_create_signal(u'courses', ['TagTranslation'])

        # Adding unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_tag_translation', ['language_code', 'master_id'])

        # Adding model 'CourseTranslation'
        db.create_table(u'courses_course_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['courses.Course'])),
        ))
        db.send_create_signal(u'courses', ['CourseTranslation'])

        # Adding unique constraint on 'CourseTranslation', fields ['language_code', 'master']
        db.create_unique(u'courses_course_translation', ['language_code', 'master_id'])

        # Deleting field 'Topic.slug'
        db.delete_column(u'courses_topic', 'slug')

        # Deleting field 'Topic.description'
        db.delete_column(u'courses_topic', 'description')

        # Deleting field 'Topic.name'
        db.delete_column(u'courses_topic', 'name')

        # Deleting field 'Course.description'
        db.delete_column(u'courses_course', 'description')

        # Deleting field 'Course.name'
        db.delete_column(u'courses_course', 'name')

        # Deleting field 'Audience.description'
        db.delete_column(u'courses_audience', 'description')

        # Deleting field 'Audience.name'
        db.delete_column(u'courses_audience', 'name')

        # Deleting field 'Skill.description'
        db.delete_column(u'courses_skill', 'description')

        # Deleting field 'Skill.name'
        db.delete_column(u'courses_skill', 'name')

        # Deleting field 'Tool.description'
        db.delete_column(u'courses_tool', 'description')

        # Deleting field 'Tool.name'
        db.delete_column(u'courses_tool', 'name')

        # Deleting field 'Module.description'
        db.delete_column(u'courses_module', 'description')

        # Deleting field 'Module.text'
        db.delete_column(u'courses_module', 'text')

        # Deleting field 'Module.name'
        db.delete_column(u'courses_module', 'name')

        # Deleting field 'Tag.description'
        db.delete_column(u'courses_tag', 'description')

        # Deleting field 'Tag.name'
        db.delete_column(u'courses_tag', 'name')


    def backwards(self, orm):
        # Removing unique constraint on 'CourseTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_course_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'TagTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_tag_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'TopicTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_topic_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ModuleTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_module_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SkillTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_skill_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ToolTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_tool_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'AudienceTranslation', fields ['language_code', 'master']
        db.delete_unique(u'courses_audience_translation', ['language_code', 'master_id'])

        # Deleting model 'AudienceTranslation'
        db.delete_table(u'courses_audience_translation')

        # Deleting model 'ToolTranslation'
        db.delete_table(u'courses_tool_translation')

        # Deleting model 'SkillTranslation'
        db.delete_table(u'courses_skill_translation')

        # Deleting model 'ModuleTranslation'
        db.delete_table(u'courses_module_translation')

        # Deleting model 'TopicTranslation'
        db.delete_table(u'courses_topic_translation')

        # Deleting model 'TagTranslation'
        db.delete_table(u'courses_tag_translation')

        # Deleting model 'CourseTranslation'
        db.delete_table(u'courses_course_translation')

        # Adding field 'Topic.slug'
        db.add_column(u'courses_topic', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='asf', max_length=50, unique=True),
                      keep_default=False)

        # Adding field 'Topic.description'
        db.add_column(u'courses_topic', 'description',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)

        # Adding field 'Topic.name'
        db.add_column(u'courses_topic', 'name',
                      self.gf('django.db.models.fields.CharField')(default='topic', max_length=1024),
                      keep_default=False)

        # Adding field 'Course.description'
        db.add_column(u'courses_course', 'description',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)

        # Adding field 'Course.name'
        db.add_column(u'courses_course', 'name',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=1024),
                      keep_default=False)

        # Adding field 'Audience.description'
        db.add_column(u'courses_audience', 'description',
                      self.gf('django.db.models.fields.TextField')(default='default'),
                      keep_default=False)

        # Adding field 'Audience.name'
        db.add_column(u'courses_audience', 'name',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=1024),
                      keep_default=False)

        # Adding field 'Skill.description'
        db.add_column(u'courses_skill', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Skill.name'
        db.add_column(u'courses_skill', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Tool.description'
        db.add_column(u'courses_tool', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Tool.name'
        db.add_column(u'courses_tool', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Module.description'
        db.add_column(u'courses_module', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Module.text'
        db.add_column(u'courses_module', 'text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Module.name'
        db.add_column(u'courses_module', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Tag.description'
        db.add_column(u'courses_tag', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Tag.name'
        db.add_column(u'courses_tag', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.audience': {
            'Meta': {'object_name': 'Audience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.audiencetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'AudienceTranslation', 'db_table': "u'courses_audience_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Audience']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
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
            'audience': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Audience']", 'null': 'True', 'blank': 'True'}),
            'completedby': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'skill': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Skill']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Tag']", 'null': 'True', 'blank': 'True'}),
            'tool': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Tool']", 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Topic']", 'null': 'True', 'blank': 'True'})
        },
        u'courses.moduletranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ModuleTranslation', 'db_table': "u'courses_module_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Module']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'courses.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.skilltranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SkillTranslation', 'db_table': "u'courses_skill_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Skill']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'courses.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.tagtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TagTranslation', 'db_table': "u'courses_tag_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Tag']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'courses.tool': {
            'Meta': {'object_name': 'Tool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courses.tooltranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ToolTranslation', 'db_table': "u'courses_tool_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Tool']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'courses.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'courses.topictranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TopicTranslation', 'db_table': "u'courses_topic_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['courses.Topic']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['courses']