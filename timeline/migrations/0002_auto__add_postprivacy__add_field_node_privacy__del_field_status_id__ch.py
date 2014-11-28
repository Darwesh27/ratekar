# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostPrivacy'
        db.create_table(u'timeline_postprivacy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'timeline', ['PostPrivacy'])

        # Adding M2M table for field include on 'PostPrivacy'
        m2m_table_name = db.shorten_name(u'timeline_postprivacy_include')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postprivacy', models.ForeignKey(orm[u'timeline.postprivacy'], null=False)),
            ('friendslist', models.ForeignKey(orm[u'social.friendslist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postprivacy_id', 'friendslist_id'])

        # Adding M2M table for field exclude on 'PostPrivacy'
        m2m_table_name = db.shorten_name(u'timeline_postprivacy_exclude')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postprivacy', models.ForeignKey(orm[u'timeline.postprivacy'], null=False)),
            ('friendslist', models.ForeignKey(orm[u'social.friendslist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postprivacy_id', 'friendslist_id'])

        # Adding field 'Node.privacy'
        db.add_column(u'timeline_node', 'privacy',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timeline.PostPrivacy']),
                      keep_default=False)

        # Deleting field 'Status.id'
        db.delete_column(u'timeline_status', u'id')


        # Changing field 'Status.node'
        db.alter_column(u'timeline_status', 'node_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Node'], primary_key=True))
        # Adding unique constraint on 'Status', fields ['node']
        db.create_unique(u'timeline_status', ['node_id'])

        # Adding field 'Post.privacy'
        db.add_column(u'timeline_post', 'privacy',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timeline.PostPrivacy']),
                      keep_default=False)

        # Deleting field 'Share.id'
        db.delete_column(u'timeline_share', u'id')

        # Adding field 'Share.node'
        db.add_column(u'timeline_share', 'node',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timeline.Node'], primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Status', fields ['node']
        db.delete_unique(u'timeline_status', ['node_id'])

        # Deleting model 'PostPrivacy'
        db.delete_table(u'timeline_postprivacy')

        # Removing M2M table for field include on 'PostPrivacy'
        db.delete_table(db.shorten_name(u'timeline_postprivacy_include'))

        # Removing M2M table for field exclude on 'PostPrivacy'
        db.delete_table(db.shorten_name(u'timeline_postprivacy_exclude'))

        # Deleting field 'Node.privacy'
        db.delete_column(u'timeline_node', 'privacy_id')

        # Adding field 'Status.id'
        db.add_column(u'timeline_status', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'Status.node'
        db.alter_column(u'timeline_status', 'node_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.Node']))
        # Deleting field 'Post.privacy'
        db.delete_column(u'timeline_post', 'privacy_id')


        # User chose to not deal with backwards NULL issues for 'Share.id'
        raise RuntimeError("Cannot reverse this migration. 'Share.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Share.id'
        db.add_column(u'timeline_share', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Deleting field 'Share.node'
        db.delete_column(u'timeline_share', 'node_id')


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
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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