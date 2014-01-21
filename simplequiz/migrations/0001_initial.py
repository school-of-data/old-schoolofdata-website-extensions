# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BadgeService'
        db.create_table(u'simplequiz_badgeservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('app_id', self.gf('django.db.models.fields.IntegerField')()),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'simplequiz', ['BadgeService'])

        # Adding model 'Answer'
        db.create_table(u'simplequiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplequiz.Question'])),
            ('correct', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'simplequiz', ['Answer'])

        # Adding model 'Question'
        db.create_table(u'simplequiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplequiz.Quiz'])),
        ))
        db.send_create_signal(u'simplequiz', ['Question'])

        # Adding model 'Quiz'
        db.create_table(u'simplequiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('badge', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('badge_service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplequiz.BadgeService'])),
            ('min_right', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'simplequiz', ['Quiz'])

        # Adding model 'Submission'
        db.create_table(u'simplequiz_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simplequiz.Quiz'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('submission', self.gf('django.db.models.fields.TextField')()),
            ('correct', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('submitted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'simplequiz', ['Submission'])


    def backwards(self, orm):
        # Deleting model 'BadgeService'
        db.delete_table(u'simplequiz_badgeservice')

        # Deleting model 'Answer'
        db.delete_table(u'simplequiz_answer')

        # Deleting model 'Question'
        db.delete_table(u'simplequiz_question')

        # Deleting model 'Quiz'
        db.delete_table(u'simplequiz_quiz')

        # Deleting model 'Submission'
        db.delete_table(u'simplequiz_submission')


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
            'badge': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'badge_service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simplequiz.BadgeService']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_right': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
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