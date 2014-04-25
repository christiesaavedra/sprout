# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table(u'public_supplier')

        # Deleting model 'Material'
        db.delete_table(u'public_material')

        # Deleting model 'Revision'
        db.delete_table(u'public_revision')

        # Deleting model 'AttributeType'
        db.delete_table(u'public_attributetype')

        # Deleting model 'ItemType'
        db.delete_table(u'public_itemtype')

        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Deleting model 'Color'
        db.delete_table(u'public_color')

        # Deleting model 'Template'
        db.delete_table(u'public_template')

        # Adding model 'Recipe'
        db.create_table(u'public_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cook_time', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cook_method', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'public.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'ingredient_id'])

        # Adding model 'Ingredient'
        db.create_table(u'public_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('glycemic_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'public', ['Ingredient'])


    def backwards(self, orm):
        # Adding model 'Supplier'
        db.create_table(u'public_supplier', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Material'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Supplier'])

        # Adding model 'Material'
        db.create_table(u'public_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Material'])

        # Adding model 'Revision'
        db.create_table(u'public_revision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Revision'])

        # Adding model 'AttributeType'
        db.create_table(u'public_attributetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['AttributeType'])

        # Adding model 'ItemType'
        db.create_table(u'public_itemtype', (
            ('abb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_non_inventory_item', self.gf('django.db.models.fields.BooleanField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('is_inventory', self.gf('django.db.models.fields.BooleanField')()),
            ('is_recoup', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['ItemType'])

        # Adding model 'Item'
        db.create_table(u'public_item', (
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Adding model 'Color'
        db.create_table(u'public_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Color'])

        # Adding model 'Template'
        db.create_table(u'public_template', (
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Template'])

        # Deleting model 'Recipe'
        db.delete_table(u'public_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_ingredients'))

        # Deleting model 'Ingredient'
        db.delete_table(u'public_ingredient')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'glycemic_index': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cook_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']