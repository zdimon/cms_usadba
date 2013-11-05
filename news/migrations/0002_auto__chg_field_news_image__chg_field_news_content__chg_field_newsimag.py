# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.image'
        db.alter_column(u'news_news', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'News.content'
        db.alter_column(u'news_news', 'content', self.gf('tinymce.models.HTMLField')())

        # Changing field 'NewsImages.image'
        db.alter_column(u'news_newsimages', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'News.image'
        db.alter_column(u'news_news', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'News.content'
        db.alter_column(u'news_news', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'NewsImages.image'
        db.alter_column(u'news_newsimages', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'news.news': {
            'Meta': {'object_name': 'News'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'news.newsimages': {
            'Meta': {'object_name': 'NewsImages'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['news']