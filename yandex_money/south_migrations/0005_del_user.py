# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Payment', fields ['order_number']
        db.delete_unique(u'yandex_money_payment', ['order_number'])


        # Changing field 'Payment.user'
        db.alter_column(u'yandex_money_payment', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True))

        # Changing field 'Payment.order_number'
        db.alter_column(u'yandex_money_payment', 'order_number', self.gf('django.db.models.fields.CharField')(max_length=64))
        # Adding unique constraint on 'Payment', fields ['shop_id', 'order_number']
        db.create_unique(u'yandex_money_payment', ['shop_id', 'order_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Payment', fields ['shop_id', 'order_number']
        db.delete_unique(u'yandex_money_payment', ['shop_id', 'order_number'])


        # Changing field 'Payment.user'
        db.alter_column(u'yandex_money_payment', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Payment.order_number'
        db.alter_column(u'yandex_money_payment', 'order_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, null=True))
        # Adding unique constraint on 'Payment', fields ['order_number']
        db.create_unique(u'yandex_money_payment', ['order_number'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'b_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'email_checked_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_billing_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_email_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'permission_granted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registered_from': ('django.db.models.fields.CharField', [], {'default': "'PLAIN'", 'max_length': '20'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'social_gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subscribed_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        'yandex_money.payment': {
            'Meta': {'ordering': "('-pub_date',)", 'unique_together': "(('shop_id', 'order_number'),)", 'object_name': 'Payment'},
            'article_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cps_email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cps_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'customer_number': ('django.db.models.fields.CharField', [], {'default': "'e9d2beae789c4cd48c63a731a8a2c5bf'", 'max_length': '64'}),
            'fail_url': ('django.db.models.fields.URLField', [], {'default': "'http://localhost:8000/pay/yk/fail/'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'order_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643'}),
            'order_number': ('django.db.models.fields.CharField', [], {'default': "'a30bbb7274674fc6a63c71fea5112a4e'", 'max_length': '64'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'pc'", 'max_length': '2'}),
            'performed_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'scid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '524627'}),
            'shop_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'shop_currency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '643', 'null': 'True', 'blank': 'True'}),
            'shop_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '43621'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'processed'", 'max_length': '16'}),
            'success_url': ('django.db.models.fields.URLField', [], {'default': "'http://localhost:8000/pay/yk/succ/'", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yandex_money']