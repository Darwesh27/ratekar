# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reputation'
        db.create_table(u'personality_reputation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='myRatings', to=orm['social.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendsRatings', to=orm['social.User'])),
            ('reputation', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'personality', ['Reputation'])

        # Adding model 'Review'
        db.create_table(u'personality_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='myReviews', to=orm['social.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendsReviews', to=orm['social.User'])),
            ('review', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('liked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'personality', ['Review'])

        # Adding model 'Trait'
        db.create_table(u'personality_trait', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'personality', ['Trait'])

        # Adding model 'TraityQuestion'
        db.create_table(u'personality_traityquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trait', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personality.Trait'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('min_cat', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'personality', ['TraityQuestion'])

        # Adding model 'Feedback'
        db.create_table(u'personality_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='myFeedbacks', to=orm['social.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendsFeedbacks', to=orm['social.User'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personality.TraityQuestion'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'personality', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'Reputation'
        db.delete_table(u'personality_reputation')

        # Deleting model 'Review'
        db.delete_table(u'personality_review')

        # Deleting model 'Trait'
        db.delete_table(u'personality_trait')

        # Deleting model 'TraityQuestion'
        db.delete_table(u'personality_traityquestion')

        # Deleting model 'Feedback'
        db.delete_table(u'personality_feedback')


    models = {
        u'personality.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendsFeedbacks'", 'to': u"orm['social.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personality.TraityQuestion']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'myFeedbacks'", 'to': u"orm['social.User']"})
        },
        u'personality.reputation': {
            'Meta': {'object_name': 'Reputation'},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendsRatings'", 'to': u"orm['social.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reputation': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'myRatings'", 'to': u"orm['social.User']"})
        },
        u'personality.review': {
            'Meta': {'object_name': 'Review'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendsReviews'", 'to': u"orm['social.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_on': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'myReviews'", 'to': u"orm['social.User']"})
        },
        u'personality.trait': {
            'Meta': {'object_name': 'Trait'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'personality.traityquestion': {
            'Meta': {'object_name': 'TraityQuestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_cat': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trait': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personality.Trait']"})
        },
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

    complete_apps = ['personality']