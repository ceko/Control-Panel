# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table('dashboard_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_logged', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dashboard', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table('dashboard_log')


    models = {
        'dashboard.log': {
            'Meta': {'object_name': 'Log'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_logged': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['dashboard']