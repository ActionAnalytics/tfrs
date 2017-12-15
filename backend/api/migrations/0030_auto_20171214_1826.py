# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 18:26
from __future__ import unicode_literals


from django.db import migrations, models
import uuid


def migrate_authorization_guid(apps, schema_editor):
    User = apps.get_model("api", "User")
    for user in User.objects.all():
        if not user.authorization_guid_old:
            user.authorization_guid_new = None
        else:
            user.authorization_guid_new = uuid(user.authorization_guid_old)
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20171213_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='authorization_guid',
            new_name='authorization_guid_old',
        ),
        migrations.AddField(
            model_name='user',
            name='authorization_guid_new',
            field=models.UUIDField(default=None, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='effective_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.RunPython(migrate_authorization_guid),
        # migrations.RunSQL(
        #     'UPDATE "user" SET '
        #     '"authorization_guid_new" = '
        #     '(CASE WHEN "authorization_guid_old" = \'\''
        #     '      THEN null'
        #     '      ELSE uuid("authorization_guid_old")'
        #     '      END)')
    ]
