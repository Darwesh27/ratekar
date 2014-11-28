# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rating'
        db.create_table(u'timeline_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Node'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.User'])),
            ('reputation', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'timeline', ['Rating'])


        # Changing field 'Post.created_on'
        db.alter_column(u'timeline_post', 'created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Deleting model 'Rating'
        db.delete_table(u'timeline_rating')


        # Changing field 'Post.created_on'
        db.alter_column(u'timeline_post', 'created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'social.friendslist': {
            'Meta': {'object_name': 'Friendslist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"})
        },
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
            'post_privacy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.PostPrivacy']", 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        u'timeline.node': {
            'Meta': {'object_name': 'Node'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Post']", 'null': 'True'}),
            'privacy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.PostPrivacy']"})
        },
        u'timeline.post': {
            'Meta': {'object_name': 'Post'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"}),
            'privacy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.PostPrivacy']"})
        },
        u'timeline.postprivacy': {
            'Meta': {'object_name': 'PostPrivacy'},
            'exclude': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'excPosts'", 'symmetrical': 'False', 'to': u"orm['social.Friendslist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'incPosts'", 'symmetrical': 'False', 'to': u"orm['social.Friendslist']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        u'timeline.rating': {
            'Meta': {'object_name': 'Rating'},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Node']"}),
            'reputation': ('django.db.models.fields.IntegerField', [], {})
        },
        u'timeline.share': {
            'Meta': {'object_name': 'Share'},
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Node']", 'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Post']"})
        },
        u'timeline.status': {
            'Meta': {'object_name': 'Status'},
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.Node']", 'primary_key': 'True'})
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