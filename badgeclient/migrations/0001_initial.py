# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BadgeService'
        db.create_table(u'badgeclient_badgeservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('app_id', self.gf('django.db.models.fields.IntegerField')()),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'badgeclient', ['BadgeService'])


    def backwards(self, orm):
        # Deleting model 'BadgeService'
        db.delete_table(u'badgeclient_badgeservice')


    models = {
        u'badgeclient.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['badgeclient']