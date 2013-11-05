# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe.image'
        db.alter_column(u'recipes_recipe', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'RecipesSteps.image'
        db.alter_column(u'recipes_recipessteps', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Recipe.image'
        db.alter_column(u'recipes_recipe', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'RecipesSteps.image'
        db.alter_column(u'recipes_recipessteps', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'authors': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Recipe']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['recipes']