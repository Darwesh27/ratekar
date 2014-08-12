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
            ('phone_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'social', ['User'])

        # Adding model 'Friendslist'
        db.create_table(u'social_friendslist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'social', ['Friendslist'])

        # Adding model 'Friendship'
        db.create_table(u'social_friendship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friends', to=orm['social.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendOf', to=orm['social.User'])),
            ('category', self.gf('django.db.models.fields.IntegerField')()),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'social', ['Friendship'])

        # Adding M2M table for field lists on 'Friendship'
        m2m_table_name = db.shorten_name(u'social_friendship_lists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('friendship', models.ForeignKey(orm[u'social.friendship'], null=False)),
            ('friendslist', models.ForeignKey(orm[u'social.friendslist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['friendship_id', 'friendslist_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'social_user')

        # Deleting model 'Friendslist'
        db.delete_table(u'social_friendslist')

        # Deleting model 'Friendship'
        db.delete_table(u'social_friendship')

        # Removing M2M table for field lists on 'Friendship'
        db.delete_table(db.shorten_name(u'social_friendship_lists'))


    models = {
        u'social.friendship': {
            'Meta': {'object_name': 'Friendship'},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendOf'", 'to': u"orm['social.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['social.Friendslist']", 'symmetrical': 'False'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friends'", 'to': u"orm['social.User']"})
        },
        u'social.friendslist': {
            'Meta': {'object_name': 'Friendslist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social.User']"})
        },
        u'social.user': {
            'Meta': {'object_name': 'User'},
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['social']