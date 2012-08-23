# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('parachute_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastedited', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('parachute', ['Project'])

        # Adding model 'Step'
        db.create_table('parachute_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('lastedited', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parachute.Project'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('parachute', ['Step'])

        # Adding model 'SVNStep'
        db.create_table('parachute_svnstep', (
            ('step_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['parachute.Step'], unique=True, primary_key=True)),
            ('command', self.gf('django.db.models.fields.CharField')(default='update', max_length=50)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('parachute', ['SVNStep'])

        # Adding model 'ScriptStep'
        db.create_table('parachute_scriptstep', (
            ('step_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['parachute.Step'], unique=True, primary_key=True)),
            ('script_location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('parachute', ['ScriptStep'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('parachute_project')

        # Deleting model 'Step'
        db.delete_table('parachute_step')

        # Deleting model 'SVNStep'
        db.delete_table('parachute_svnstep')

        # Deleting model 'ScriptStep'
        db.delete_table('parachute_scriptstep')


    models = {
        'parachute.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastedited': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'parachute.scriptstep': {
            'Meta': {'object_name': 'ScriptStep', '_ormbases': ['parachute.Step']},
            'script_location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'step_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['parachute.Step']", 'unique': 'True', 'primary_key': 'True'})
        },
        'parachute.step': {
            'Meta': {'object_name': 'Step'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastedited': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parachute.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'parachute.svnstep': {
            'Meta': {'object_name': 'SVNStep', '_ormbases': ['parachute.Step']},
            'command': ('django.db.models.fields.CharField', [], {'default': "'update'", 'max_length': '50'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'step_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['parachute.Step']", 'unique': 'True', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['parachute']