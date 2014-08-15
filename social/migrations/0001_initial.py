# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'social_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True, null=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'social', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'social_user')


    models = {
        u'social.user': {
            'Meta': {'object_name': 'User'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['social']