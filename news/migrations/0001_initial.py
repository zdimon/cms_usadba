# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'news_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'news', ['News'])

        # Adding model 'NewsImages'
        db.create_table(u'news_newsimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.News'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'news', ['NewsImages'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'news_news')

        # Deleting model 'NewsImages'
        db.delete_table(u'news_newsimages')


    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'news.newsimages': {
            'Meta': {'object_name': 'NewsImages'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['news']