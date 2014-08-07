# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.status'
        db.add_column(u'profilemap_person', 'status',
                      self.gf('django.db.models.fields.CharField')(default='S', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.status'
        db.delete_column(u'profilemap_person', 'status')


    models = {
        u'profilemap.person': {
            'Meta': {'object_name': 'Person'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['profilemap']