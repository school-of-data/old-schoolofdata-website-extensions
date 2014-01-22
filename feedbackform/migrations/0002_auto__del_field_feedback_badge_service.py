# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feedback.badge_service'
        db.delete_column(u'feedbackform_feedback', 'badge_service_id')


    def backwards(self, orm):
        # Adding field 'Feedback.badge_service'
        db.add_column(u'feedbackform_feedback', 'badge_service',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['badgeclient.BadgeService'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'feedbackform.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empowered': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improve': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'learned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organise': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'testimonial': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'useful': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'worthwile': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['feedbackform']