# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'timeline_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.User'])),
            ('kind', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'timeline', ['Post'])

        # Adding model 'Node'
        db.create_table(u'timeline_node', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Post'], null=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.User'])),
            ('kind', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'timeline', ['Node'])

        # Adding model 'ThoughtDraft'
        db.create_table(u'timeline_thoughtdraft', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Node'])),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'timeline', ['ThoughtDraft'])

        # Adding model 'Status'
        db.create_table(u'timeline_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Node'])),
        ))
        db.send_create_signal(u'timeline', ['Status'])

        # Adding model 'Share'
        db.create_table(u'timeline_share', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Post'])),
        ))
        db.send_create_signal(u'timeline', ['Share'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'timeline_post')

        # Deleting model 'Node'
        db.delete_table(u'timeline_node')

        # Deleting model 'ThoughtDraft'
        db.delete_table(u'timeline_thoughtdraft')

        # Deleting model 'Status'
        db.delete_table(u'timeline_status')

        # Deleting model 'Share'
        db.delete_table(u'timeline_share')


    models = {
        u'social.user': {
            'Meta': {'object_name': 'User'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'timeline.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Post']", 'null': 'True'})
        },
        u'timeline.post': {
            'Meta': {'object_name': 'Post'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"})
        },
        u'timeline.share': {
            'Meta': {'object_name': 'Share'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Post']"})
        },
        u'timeline.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Node']"})
        },
        u'timeline.thoughtdraft': {
            'Meta': {'object_name': 'ThoughtDraft'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Node']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['timeline']