# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'recipes_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
            ('authors', self.gf('django.db.models.fields.TextField')()),
            ('ingradients', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'recipes', ['Recipe'])

        # Adding model 'RecipesSteps'
        db.create_table(u'recipes_recipessteps', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'recipes', ['RecipesSteps'])

        # Adding model 'RecipesComments'
        db.create_table(u'recipes_recipescomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('is_pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'recipes', ['RecipesComments'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table(u'recipes_recipe')

        # Deleting model 'RecipesSteps'
        db.delete_table(u'recipes_recipessteps')

        # Deleting model 'RecipesComments'
        db.delete_table(u'recipes_recipescomments')


    models = {
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'authors': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'ingradients': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'recipes.recipescomments': {
            'Meta': {'object_name': 'RecipesComments'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"})
        },
        u'recipes.recipessteps': {
            'Meta': {'object_name': 'RecipesSteps'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['recipes']