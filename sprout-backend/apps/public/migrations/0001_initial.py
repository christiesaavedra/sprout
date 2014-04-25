# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'public_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Adding model 'Template'
        db.create_table(u'public_template', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute2', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Template'])

        # Adding model 'Color'
        db.create_table(u'public_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Color'])

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

        # Adding model 'Supplier'
        db.create_table(u'public_supplier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Material'])),
        ))
        db.send_create_signal(u'public', ['Supplier'])

        # Adding model 'ItemType'
        db.create_table(u'public_itemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('is_recoup', self.gf('django.db.models.fields.BooleanField')()),
            ('is_inventory', self.gf('django.db.models.fields.BooleanField')()),
            ('abb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_non_inventory_item', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'public', ['ItemType'])

        # Adding model 'AttributeType'
        db.create_table(u'public_attributetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['AttributeType'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Deleting model 'Template'
        db.delete_table(u'public_template')

        # Deleting model 'Color'
        db.delete_table(u'public_color')

        # Deleting model 'Material'
        db.delete_table(u'public_material')

        # Deleting model 'Revision'
        db.delete_table(u'public_revision')

        # Deleting model 'Supplier'
        db.delete_table(u'public_supplier')

        # Deleting model 'ItemType'
        db.delete_table(u'public_itemtype')

        # Deleting model 'AttributeType'
        db.delete_table(u'public_attributetype')


    models = {
        u'public.attributetype': {
            'Meta': {'object_name': 'AttributeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'abb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inventory': ('django.db.models.fields.BooleanField', [], {}),
            'is_non_inventory_item': ('django.db.models.fields.BooleanField', [], {}),
            'is_recoup': ('django.db.models.fields.BooleanField', [], {}),
            'is_template': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.revision': {
            'Meta': {'object_name': 'Revision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'public.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Material']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.template': {
            'Meta': {'object_name': 'Template'},
            'attribute1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attribute2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']