# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0022_auto_20171116_2335'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='organization',
            table='organization',
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('create_timestamp',
                 models.DateTimeField(auto_now_add=True, null=True)),
                ('update_timestamp',
                 models.DateTimeField(auto_now=True, null=True)),
                ('type', models.CharField(max_length=25)),
                ('description',
                 models.CharField(blank=True, max_length=1000, null=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('displayOrder', models.IntegerField()),
            ],
            options={
                'db_table': 'organization_type',
            },
        ),
        migrations.RemoveField(
            model_name='userfavourite',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='userfavourite',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='userfavourite',
            name='userFK',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='tradeEffectiveDate',
            new_name='trade_effective_date',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newTradeEffectiveDate',
            new_name='trade_effective_date',
        ),
        migrations.RenameField(
            model_name='credittradestatus',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='credittradetype',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='credittradezeroreason',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='organizationactionstype',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='organizationbalance',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='organizationstatus',
            old_name='effectiveDate',
            new_name='effective_date',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='creditTradeStatusFK',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='creditTradeTypeFK',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='creditTradeZeroReasonFK',
            new_name='zero_reason',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='initiatorFK',
            new_name='initiator',
        ),
        migrations.RenameField(
            model_name='credittrade',
            old_name='respondentFK',
            new_name='respondent',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='creditTradeFK',
            new_name='credit_trade',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='creditTradeStatusFK',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='creditTradeTypeFK',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newCreditTradeZeroReasonFK',
            new_name='zero_reason',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='newRespondentFK',
            new_name='respondent',
        ),
        migrations.RenameField(
            model_name='credittradehistory',
            old_name='userFK',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='fuelSupplierActionsTypeFK',
            new_name='actions_type',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='fuelSupplierStatusFK',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='organizationattachment',
            old_name='fuelSupplierFK',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='organizationbalance',
            old_name='creditTradeFK',
            new_name='credit_trade',
        ),
        migrations.RenameField(
            model_name='organizationbalance',
            old_name='fuelSupplierFK',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='organizationhistory',
            old_name='fuelSupplierFK',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='rolepermission',
            old_name='permissionFK',
            new_name='permission',
        ),
        migrations.RenameField(
            model_name='rolepermission',
            old_name='roleFK',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='roleFK',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='userFK',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='credittrade',
            name='initiator',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='initiator_credit_trades',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='credittrade',
            name='respondent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='respondent_credit_trades',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='credittrade',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trades',
                                    to='api.CreditTradeStatus'),
        ),
        migrations.AlterField(
            model_name='credittrade',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trades',
                                    to='api.CreditTradeType'),
        ),
        migrations.AlterField(
            model_name='credittrade',
            name='zero_reason',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trades',
                                    to='api.CreditTradeZeroReason'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='credit_trade',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.CreditTrade'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='respondent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.CreditTradeStatus'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.CreditTradeType'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='credittradehistory',
            name='zero_reason',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='credit_trade_histories',
                                    to='api.CreditTradeZeroReason'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='actions_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='organizations',
                                    to='api.OrganizationActionsType'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='organizations',
                                    to='api.OrganizationStatus'),
        ),
        migrations.AlterField(
            model_name='organizationattachment',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='attachments',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationbalance',
            name='credit_trade',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='balances',
                                    to='api.CreditTrade'),
        ),
        migrations.AlterField(
            model_name='organizationbalance',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='balances',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationhistory',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='history',
                                    to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='rolepermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='role_permissions',
                                    to='api.Permission'),
        ),
        migrations.AlterField(
            model_name='rolepermission',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='role_permissions',
                                    to='api.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, blank=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='users',
                                    to='api.Organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='user_roles', to='api.Role'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='user_roles', to='api.User'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organization_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organization_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationactionstype',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationactionstype_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationactionstype',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationactionstype_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationattachment',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationattachment_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationattachment',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationattachment_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationbalance',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationbalance_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationbalance',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationbalance_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationhistory',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationhistory_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationhistory',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationhistory_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationstatus_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationstatus_UPDATE_USER',
                                    to='api.User'),
        ),
        migrations.AlterModelTable(
            name='organizationactionstype',
            table='organization_actions_type',
        ),
        migrations.AlterModelTable(
            name='organizationattachment',
            table='organization_attachment',
        ),
        migrations.AlterModelTable(
            name='organizationbalance',
            table='organization_balance',
        ),
        migrations.AlterModelTable(
            name='organizationhistory',
            table='organization_history',
        ),
        migrations.AlterModelTable(
            name='organizationstatus',
            table='organization_status',
        ),
        migrations.DeleteModel(
            name='UserFavourite',
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationtype_CREATE_USER',
                                    to='api.User'),
        ),
        migrations.AddField(
            model_name='organizationtype',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='api_organizationtype_UPDATE_USER',
                                    to='api.User'),
        ),
        # migrations.AddField(
        #     model_name='organization',
        #     name='type',
        #     field=models.ForeignKey(default=1,
        #                             on_delete=django.db.models.deletion.CASCADE,
        #                             related_name='organizations',
        #                             to='api.OrganizationType'),
        #     preserve_default=False,
        # ),
    ]
