# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BadgeService'
        db.delete_table(u'simplequiz_badgeservice')


        # Changing field 'Quiz.badge_service'
        db.alter_column(u'simplequiz_quiz', 'badge_service_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['badgeclient.BadgeService'], null=True))

    def backwards(self, orm):
        # Adding model 'BadgeService'
        db.create_table(u'simplequiz_badgeservice', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('app_id', self.gf('django.db.models.fields.IntegerField')()),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'simplequiz', ['BadgeService'])


        # Changing field 'Quiz.badge_service'
        db.alter_column(u'simplequiz_quiz', 'badge_service_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplequiz.BadgeService'], null=True))

    models = {
        u'badgeclient.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'simplequiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.Question']"})
        },
        u'simplequiz.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.Quiz']"})
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
        },
        u'simplequiz.submission': {
            'Meta': {'object_name': 'Submission'},
            'correct': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.Quiz']"}),
            'submission': ('django.db.models.fields.TextField', [], {}),
            'submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['simplequiz']