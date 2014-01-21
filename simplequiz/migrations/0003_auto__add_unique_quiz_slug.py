# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Quiz', fields ['slug']
        db.create_unique(u'simplequiz_quiz', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Quiz', fields ['slug']
        db.delete_unique(u'simplequiz_quiz', ['slug'])


    models = {
        u'simplequiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.Question']"})
        },
        u'simplequiz.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
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
            'badge_service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.BadgeService']", 'null': 'True', 'blank': 'True'}),
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