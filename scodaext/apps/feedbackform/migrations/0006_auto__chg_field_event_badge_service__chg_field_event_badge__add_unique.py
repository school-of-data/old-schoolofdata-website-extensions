# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.badge_service'
        db.alter_column(u'feedbackform_event', 'badge_service_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['badgeclient.BadgeService'], null=True))

        # Changing field 'Event.badge'
        db.alter_column(u'feedbackform_event', 'badge', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))
        # Adding unique constraint on 'Event', fields ['name']
        db.create_unique(u'feedbackform_event', ['name'])

        # Deleting field 'Feedback.event'
        db.delete_column(u'feedbackform_feedback', 'event')


    def backwards(self, orm):
        # Removing unique constraint on 'Event', fields ['name']
        db.delete_unique(u'feedbackform_event', ['name'])


        # Changing field 'Event.badge_service'
        db.alter_column(u'feedbackform_event', 'badge_service_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['badgeclient.BadgeService']))

        # Changing field 'Event.badge'
        db.alter_column(u'feedbackform_event', 'badge', self.gf('django.db.models.fields.SlugField')(default=None, max_length=50))
        # Adding field 'Feedback.event'
        db.add_column(u'feedbackform_feedback', 'event',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    models = {
        u'badgeclient.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'feedbackform.event': {
            'Meta': {'object_name': 'Event'},
            'badge': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'badge_service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['badgeclient.BadgeService']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'feedbackform.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empowered': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improve': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'learned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organise': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'testimonial': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'useful': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'worthwhile': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['feedbackform']