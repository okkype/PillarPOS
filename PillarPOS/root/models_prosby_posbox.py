# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountAccount(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, db_column='user_type')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    shortcut = models.CharField(max_length=12, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    currency_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    level = models.IntegerField(blank=True, null=True)
    currency_mode = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountConsolRel(models.Model):
    child = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    parent = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_consol_rel'
        unique_together = (('child', 'parent'),)


class AccountAccountFinancialReport(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        unique_together = (('account', 'report_line'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    currency_id = models.IntegerField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, db_column='user_type')
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    shortcut = models.CharField(max_length=12, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    nocreate = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateTaxRel(models.Model):
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=32)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    close_method = models.CharField(max_length=-1)
    report_type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccountTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_type_rel'
        unique_together = (('journal', 'account'),)


class AccountAddtmplWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cparent = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_addtmpl_wizard'


class AccountAgedTrialBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_length = models.IntegerField()
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    direction_selection = models.CharField(max_length=-1)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceJournalRel(models.Model):
    account = models.ForeignKey(AccountAgedTrialBalance, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountAnalyticAccount(models.Model):
    code = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    quantity_max = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    template = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticBalance(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    empty_acc = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_balance'


class AccountAnalyticChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_chart'


class AccountAnalyticCostLedger(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_cost_ledger'


class AccountAnalyticCostLedgerJournalReport(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_cost_ledger_journal_report'


class AccountAnalyticInvertedBalance(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_inverted_balance'


class AccountAnalyticJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal'


class AccountAnalyticJournalName(models.Model):
    journal_line = models.ForeignKey('AccountAnalyticJournalReport', models.DO_NOTHING)
    journal_print = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal_name'
        unique_together = (('journal_line', 'journal_print'),)


class AccountAnalyticJournalReport(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal_report'


class AccountAnalyticLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=8, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING)
    currency_id = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAutomaticReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    power = models.IntegerField()
    max_amount = models.FloatField(blank=True, null=True)
    unreconciled = models.IntegerField(blank=True, null=True)
    reconciled = models.IntegerField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    allow_write_off = models.NullBooleanField()
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_automatic_reconcile'


class AccountBalanceReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.ForeignKey(AccountBalanceReport, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankAccountsWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('WizardMultiChartsAccounts', models.DO_NOTHING)
    acc_name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_accounts_wizard'


class AccountBankStatement(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    name = models.CharField(max_length=-1, blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    journal_entry = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    pos_statement = models.ForeignKey('PosOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashboxLine(models.Model):
    bank_statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    pieces = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    number_closing = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    number_opening = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountCentralJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_central_journal'


class AccountCentralJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountCentralJournal, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_central_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountChangeCurrency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_change_currency'


class AccountChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, db_column='fiscalyear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart'


class AccountChartTemplate(models.Model):
    property_account_income_opening = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income_opening', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    visible = models.NullBooleanField()
    tax_code_root = models.ForeignKey('AccountTaxCodeTemplate', models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_payable', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    bank_account_view = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense_categ', blank=True, null=True)
    property_account_expense_opening = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense_opening', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income_categ', blank=True, null=True)
    code_digits = models.IntegerField()
    name = models.CharField(max_length=-1)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense', blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_receivable', blank=True, null=True)
    account_root = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonAccountReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.ForeignKey(AccountCommonAccountReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonJournalReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.ForeignKey(AccountCommonJournalReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.ForeignKey(AccountCommonPartnerReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.ForeignKey(AccountCommonReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountConfigSettings(models.Model):
    date_stop = models.DateField()
    sale_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    module_account_voucher = models.NullBooleanField()
    module_account_asset = models.NullBooleanField()
    period = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_account_accountant = models.NullBooleanField()
    module_account_followup = models.NullBooleanField()
    purchase_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    has_chart_of_accounts = models.NullBooleanField()
    sale_refund_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    module_account_budget = models.NullBooleanField()
    date_start = models.DateField()
    purchase_refund_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group_check_supplier_invoice_total = models.NullBooleanField()
    group_multi_currency = models.NullBooleanField()
    group_proforma_invoices = models.NullBooleanField()
    default_purchase_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, db_column='default_purchase_tax', blank=True, null=True)
    module_product_email_template = models.NullBooleanField()
    has_default_company = models.NullBooleanField()
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    decimal_precision = models.IntegerField(blank=True, null=True)
    default_sale_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, db_column='default_sale_tax', blank=True, null=True)
    has_fiscal_year = models.NullBooleanField()
    module_account_payment = models.NullBooleanField()
    sale_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, db_column='sale_tax', blank=True, null=True)
    purchase_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, db_column='purchase_tax', blank=True, null=True)
    module_account_check_writing = models.NullBooleanField()
    code_digits = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    group_analytic_accounting = models.NullBooleanField()
    module_payment_paypal = models.NullBooleanField()
    module_payment_buckaroo = models.NullBooleanField()
    module_payment_adyen = models.NullBooleanField()
    module_payment_ogone = models.NullBooleanField()
    module_purchase_analytic_plans = models.NullBooleanField()
    group_analytic_account_for_purchases = models.NullBooleanField()
    group_analytic_account_for_sales = models.NullBooleanField()
    module_sale_analytic_plans = models.NullBooleanField()
    group_payment_options = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_config_settings'


class AccountFinancialReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    account_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    style_overwrite = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    display_detail = models.CharField(max_length=-1, blank=True, null=True)
    sign = models.IntegerField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_report'


class AccountFiscalPosition(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    auto_apply = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vat_required = models.NullBooleanField()
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    code = models.CharField(max_length=6)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    end_journal_period = models.ForeignKey('AccountJournalPeriod', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear'


class AccountFiscalyearClose(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    report_name = models.CharField(max_length=-1)
    fy2 = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    fy = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear_close'


class AccountFiscalyearCloseState(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fy = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear_close_state'


class AccountGeneralJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_general_journal'


class AccountGeneralJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountGeneralJournal, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_general_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    date_start = models.DateField()
    charts = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    period = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    has_default_company = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_installer'


class AccountInvoice(models.Model):
    comment = models.TextField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    check_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, db_column='payment_term', blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_column='fiscal_position', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    supplier_invoice_number = models.CharField(max_length=-1, blank=True, null=True)
    reference_type = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    internal_number = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    reconciled = models.NullBooleanField()
    residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    date_invoice = models.DateField(blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    sent = models.NullBooleanField()
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('CrmCaseSection', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'company', 'journal', 'type'),)


class AccountInvoiceCancel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_cancel'


class AccountInvoiceConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_confirm'


class AccountInvoiceLine(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    uos = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    name = models.TextField()
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_line'


class AccountInvoiceLineTax(models.Model):
    invoice_line = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_line_tax'
        unique_together = (('invoice_line', 'tax'),)


class AccountInvoiceRefund(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    filter_refund = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_refund'


class AccountInvoiceTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    manual = models.NullBooleanField()
    base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    base = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_invoice_tax'


class AccountJournal(models.Model):
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)
    internal_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    cash_control = models.NullBooleanField()
    centralisation = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=32)
    default_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    default_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    allow_date = models.NullBooleanField()
    update_posted = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    analytic_journal = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING, blank=True, null=True)
    with_last_closing_balance = models.NullBooleanField()
    entry_posted = models.NullBooleanField()
    group_invoice_lines = models.NullBooleanField()
    self_checkout_payment_method = models.NullBooleanField()
    journal_user = models.NullBooleanField()
    amount_authorized_diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'company'), ('name', 'company'),)


class AccountJournalAccountVatDeclarationRel(models.Model):
    account_vat_declaration = models.ForeignKey('AccountVatDeclaration', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_vat_declaration_rel'
        unique_together = (('account_vat_declaration', 'account_journal'),)


class AccountJournalAccountingReportRel(models.Model):
    accounting_report = models.ForeignKey('AccountingReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_accounting_report_rel'
        unique_together = (('accounting_report', 'account_journal'),)


class AccountJournalCashboxLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    pieces = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_cashbox_line'


class AccountJournalGroupRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_group_rel'
        unique_together = (('journal', 'group'),)


class AccountJournalPeriod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_period'


class AccountJournalSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_select'


class AccountJournalTypeRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    type = models.ForeignKey(AccountAccountType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_type_rel'
        unique_together = (('journal', 'type'),)


class AccountModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    legend = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_model'


class AccountModelLine(models.Model):
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_maturity = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_model_line'


class AccountMove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    date = models.DateField()
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    to_check = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveBankReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_bank_reconcile'


class AccountMoveLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    reconcile_partial = models.ForeignKey('AccountMoveReconcile', models.DO_NOTHING, blank=True, null=True)
    blocked = models.NullBooleanField()
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    centralisation = models.CharField(max_length=8, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    reconcile_ref = models.CharField(max_length=-1, blank=True, null=True)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    reconcile = models.ForeignKey('AccountMoveReconcile', models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trans_nbr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile'


class AccountMoveLineReconcileSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_select'


class AccountMoveLineReconcileWriteoff(models.Model):
    comment = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_p = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_writeoff'


class AccountMoveLineRelation(models.Model):
    move = models.ForeignKey('AccountStatementFromInvoiceLines', models.DO_NOTHING)
    line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_relation'
        unique_together = (('move', 'line'),)


class AccountMoveLineUnreconcileSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_unreconcile_select'


class AccountMoveReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    opening_reconciliation = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_move_reconcile'


class AccountOpenClosedFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_open_closed_fiscalyear'


class AccountPartnerBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    display_partner = models.CharField(max_length=-1, blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    result_selection = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_partner_balance'


class AccountPartnerBalanceJournalRel(models.Model):
    account = models.ForeignKey(AccountPartnerBalance, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_partner_balance_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountPartnerLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    initial_balance = models.NullBooleanField()
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    page_split = models.NullBooleanField()
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_partner_ledger'


class AccountPartnerLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountPartnerLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_partner_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountPartnerReconcileProcess(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    next_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    to_reconcile = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    today_reconciled = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partner_reconcile_process'


class AccountPaymentTerm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    days2 = models.IntegerField()
    days = models.IntegerField()
    value = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountPeriod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    code = models.CharField(max_length=12, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    date_start = models.DateField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    special = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_period'
        unique_together = (('name', 'company'),)


class AccountPeriodClose(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    sure = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_period_close'


class AccountPrintJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sort_selection = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_print_journal'


class AccountPrintJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountPrintJournal, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_print_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportGeneralLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    initial_balance = models.NullBooleanField()
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    target_move = models.CharField(max_length=-1)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    sortby = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    landscape = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountReportGeneralLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountSequenceFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    sequence_main = models.ForeignKey('IrSequence', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_sequence_fiscalyear'


class AccountStateOpen(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_state_open'


class AccountStatementFromInvoiceLines(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_statement_from_invoice_lines'


class AccountStatementOperationTemplate(models.Model):
    amount_type = models.CharField(max_length=-1)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_statement_operation_template'


class AccountSubscription(models.Model):
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)
    period_nbr = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_start = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period_total = models.IntegerField()
    state = models.CharField(max_length=-1)
    period_type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_subscription'


class AccountSubscriptionGenerate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'account_subscription_generate'


class AccountSubscriptionLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    subscription = models.ForeignKey(AccountSubscription, models.DO_NOTHING)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_subscription_line'


class AccountTax(models.Model):
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account_analytic_paid = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    ref_tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account_paid = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    base_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    child_depend = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    ref_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    applicable_type = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    python_compute_inv = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    ref_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    account_analytic_collected = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ref_base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    account_collected = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    python_compute = models.TextField(blank=True, null=True)
    tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_include = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company'),)


class AccountTaxChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_tax_chart'


class AccountTaxCode(models.Model):
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sign = models.FloatField()
    notprintable = models.NullBooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_code'


class AccountTaxCodeTemplate(models.Model):
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    sign = models.FloatField()
    notprintable = models.NullBooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_code_template'


class AccountTaxTemplate(models.Model):
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    ref_tax_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    base_sign = models.FloatField(blank=True, null=True)
    child_depend = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    applicable_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    ref_base_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    tax_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    python_compute_inv = models.TextField(blank=True, null=True)
    ref_tax_sign = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    ref_base_sign = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    base_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    account_paid = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_collected = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    python_compute = models.TextField(blank=True, null=True)
    tax_sign = models.FloatField(blank=True, null=True)
    price_include = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_tax_template'


class AccountTemplateFinancialReport(models.Model):
    account_template = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    report_line = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_template_financial_report'
        unique_together = (('account_template', 'report_line'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AccountUnreconcileReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile_reconcile'


class AccountUseModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_use_model'


class AccountUseModelRelation(models.Model):
    account = models.ForeignKey(AccountUseModel, models.DO_NOTHING)
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_use_model_relation'
        unique_together = (('account', 'model'),)


class AccountVatDeclaration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    based_on = models.CharField(max_length=-1)
    display_detail = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    chart_tax = models.ForeignKey(AccountTaxCode, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_vat_declaration'


class AccountVoucher(models.Model):
    comment = models.CharField(max_length=-1)
    date_due = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_multi_currency = models.NullBooleanField()
    number = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    narration = models.TextField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_rate_currency_id = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    pay_now = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    pre_line = models.NullBooleanField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    payment_option = models.CharField(max_length=-1)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    payment_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    name = models.CharField(max_length=-1, blank=True, null=True)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_voucher'


class AccountVoucherLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount_unreconciled = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    untax_amount = models.FloatField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    voucher = models.ForeignKey(AccountVoucher, models.DO_NOTHING)
    amount_original = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_voucher_line'


class AccountingReport(models.Model):
    period_to_cmp = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to_cmp', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_from_cmp = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from_cmp', blank=True, null=True)
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    fiscalyear_id_cmp = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, db_column='fiscalyear_id_cmp', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    label_filter = models.CharField(max_length=-1, blank=True, null=True)
    filter_cmp = models.CharField(max_length=-1)
    enable_filter = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    filter = models.CharField(max_length=-1)
    date_from_cmp = models.DateField(blank=True, null=True)
    debit_credit = models.NullBooleanField()
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'accounting_report'


class BaseConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_google_drive = models.NullBooleanField()
    module_base_import = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_portal = models.NullBooleanField()
    module_google_calendar = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    module_share = models.NullBooleanField()
    font = models.ForeignKey('ResFont', models.DO_NOTHING, db_column='font', blank=True, null=True)
    module_auth_oauth = models.NullBooleanField()
    module_multi_company = models.NullBooleanField()
    alias_domain = models.CharField(max_length=-1, blank=True, null=True)
    auth_signup_reset_password = models.NullBooleanField()
    auth_signup_uninvited = models.NullBooleanField()
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_config_settings'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    file_type = models.CharField(max_length=-1, blank=True, null=True)
    file_name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportTestsModelsChar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsM2O(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    othervalue = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    somevalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    format = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField()
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleConfiguration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_configuration'


class BaseModuleUpdate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BaseSetupTerminology(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'base_setup_terminology'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BoardCreate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    menu_parent = models.ForeignKey('IrUiMenu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_create'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class CashBoxIn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_in'


class CashBoxOut(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=-1, blank=True, null=True)
    new_passwd = models.CharField(max_length=-1, blank=True, null=True)
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class CrmCaseSection(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=True, null=True)
    working_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    complete_name = models.CharField(max_length=256, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    change_responsible = models.NullBooleanField()
    name = models.CharField(max_length=64)
    reply_to = models.CharField(max_length=64, blank=True, null=True)
    use_quotations = models.NullBooleanField()
    invoiced_target = models.IntegerField(blank=True, null=True)
    invoiced_forecast = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_case_section'


class DecimalPrecision(models.Model):
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DecimalPrecisionTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    float_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    float_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision_test'


class EmailTemplate(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey(EmailTemplate, models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey(EmailTemplatePreview, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class FetchmailConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_config_settings'


class FetchmailServer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    port = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=-1, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    attach = models.NullBooleanField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, blank=True, null=True)
    user = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    is_ssl = models.NullBooleanField()
    server = models.CharField(max_length=-1, blank=True, null=True)
    original = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class ImChatMessage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to = models.ForeignKey('ImChatSession', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    from_field = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='from_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'im_chat_message'


class ImChatPresence(models.Model):
    status = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    last_poll = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'im_chat_presence'


class ImChatSession(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_chat_session'


class ImChatSessionResUsersRel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    session = models.ForeignKey(ImChatSession, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_chat_session_res_users_rel'


class IrActClient(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    params_store = models.BinaryField(blank=True, null=True)
    tag = models.CharField(max_length=-1)
    context = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parser = models.CharField(max_length=-1, blank=True, null=True)
    header = models.NullBooleanField()
    report_type = models.CharField(max_length=-1)
    attachment = models.CharField(max_length=-1, blank=True, null=True)
    report_sxw_content_data = models.BinaryField(blank=True, null=True)
    report_xml = models.CharField(max_length=-1, blank=True, null=True)
    report_rml_content_data = models.BinaryField(blank=True, null=True)
    auto = models.NullBooleanField()
    report_file = models.CharField(max_length=-1, blank=True, null=True)
    multi = models.NullBooleanField()
    report_xsl = models.CharField(max_length=-1, blank=True, null=True)
    report_rml = models.CharField(max_length=-1, blank=True, null=True)
    report_name = models.CharField(max_length=-1)
    attachment_use = models.NullBooleanField()
    model = models.CharField(max_length=-1)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    printing_printer = models.ForeignKey('PrintingPrinter', models.DO_NOTHING, blank=True, null=True)
    printer_tray = models.ForeignKey('PrintingTray', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    code = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    ref_object = models.CharField(max_length=128, blank=True, null=True)
    id_object = models.CharField(max_length=128, blank=True, null=True)
    crud_model_name = models.CharField(max_length=-1, blank=True, null=True)
    use_relational_model = models.CharField(max_length=-1)
    use_create = models.CharField(max_length=-1)
    wkf_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    wkf_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    id_value = models.CharField(max_length=-1, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    link_new_record = models.NullBooleanField()
    wkf_transition = models.ForeignKey('WkfTransition', models.DO_NOTHING, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    use_write = models.CharField(max_length=-1)
    wkf_model_name = models.CharField(max_length=-1, blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    write_expression = models.CharField(max_length=-1, blank=True, null=True)
    menu_ir_values = models.ForeignKey('IrValues', models.DO_NOTHING, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey(EmailTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActUrl(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    view_type = models.CharField(max_length=-1)
    src_model = models.CharField(max_length=-1, blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    auto_refresh = models.IntegerField(blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    multi = models.NullBooleanField()
    target = models.CharField(max_length=-1, blank=True, null=True)
    auto_search = models.NullBooleanField()
    res_id = models.IntegerField(blank=True, null=True)
    filter = models.NullBooleanField()
    limit = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    multi = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    action_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    datas_fname = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    store_fname = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    key = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrConfigParameterGroupsRel(models.Model):
    icp = models.ForeignKey(IrConfigParameter, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter_groups_rel'
        unique_together = (('icp', 'group'),)


class IrCron(models.Model):
    function = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    interval_type = models.CharField(max_length=-1, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    doall = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrDefault(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    ref_table = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    field_tbl = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    field_name = models.CharField(max_length=-1, blank=True, null=True)
    page = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    resource = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFieldsConverter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_fields_converter'


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    level = models.CharField(max_length=-1, blank=True, null=True)
    line = models.CharField(max_length=-1)
    dbname = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    func = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=-1)
    message = models.TextField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    smtp_encryption = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    smtp_port = models.IntegerField()
    smtp_host = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    smtp_pass = models.CharField(max_length=64, blank=True, null=True)
    smtp_debug = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    smtp_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    model = models.CharField(unique=True, max_length=-1)
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    perm_read = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    perm_unlink = models.NullBooleanField()
    perm_write = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.NullBooleanField()
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    type = models.CharField(max_length=1)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    noupdate = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('name', 'module'),)


class IrModelFields(models.Model):
    model = models.CharField(max_length=-1)
    model_0 = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model_id')  # Field renamed because of name conflict.
    name = models.CharField(max_length=-1)
    relation = models.CharField(max_length=-1, blank=True, null=True)
    select_level = models.CharField(max_length=-1)
    field_description = models.CharField(max_length=-1)
    ttype = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    relation_field = models.CharField(max_length=-1, blank=True, null=True)
    translate = models.NullBooleanField()
    serialization_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    on_delete = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    selection = models.CharField(max_length=-1, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    readonly = models.NullBooleanField()
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    selectable = models.NullBooleanField()
    required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ir_model_fields'


class IrModelFieldsGroupRel(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelRelation(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    author = models.CharField(max_length=-1, blank=True, null=True)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    latest_version = models.CharField(max_length=-1, blank=True, null=True)
    shortdesc = models.CharField(max_length=-1, blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.NullBooleanField()
    demo = models.NullBooleanField()
    web = models.NullBooleanField()
    license = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.NullBooleanField()
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    maintainer = models.CharField(max_length=-1, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrProperty(models.Model):
    value_text = models.TextField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fields = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_reference = models.CharField(max_length=-1, blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    res_id = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    domain_force = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    global_field = models.NullBooleanField(db_column='global')  # Field renamed because it was a Python reserved word.
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    perm_read = models.NullBooleanField()
    perm_unlink = models.NullBooleanField()
    perm_write = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    number_next = models.IntegerField()
    implementation = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    padding = models.IntegerField()
    number_increment = models.IntegerField()
    prefix = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    suffix = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence_type'


class IrServerObjectLines(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    col1 = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='col1')
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, db_column='lang', blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_translation'


class IrUiMenu(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    web_icon_data = models.BinaryField(blank=True, null=True)
    needaction_enabled = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    icon = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    web_icon_hover = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    web_icon = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    web_icon_hover_data = models.BinaryField(blank=True, null=True)
    mail_group = models.ForeignKey('MailGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    arch = models.TextField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    priority = models.IntegerField()
    mode = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    model = models.CharField(max_length=-1, blank=True, null=True)
    model_data = models.ForeignKey(IrModelData, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    field_parent = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING)
    arch = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class IrValues(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    key2 = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    key = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1)  # Field renamed because of name conflict.
    res_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_values'


class LedgerJournalRel(models.Model):
    ledger = models.ForeignKey(AccountAnalyticCostLedgerJournalReport, models.DO_NOTHING)
    journal = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ledger_journal_rel'
        unique_together = (('ledger', 'journal'),)


class MailAlias(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_defaults = models.TextField()
    alias_contact = models.CharField(max_length=-1)
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias_name = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailComposeMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    no_auto_thread = models.NullBooleanField()
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    notify = models.NullBooleanField()
    active_domain = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    composition_mode = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    is_log = models.NullBooleanField()
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    model = models.CharField(max_length=128, blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    use_active_domain = models.NullBooleanField()
    type = models.CharField(max_length=12, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    template = models.ForeignKey(EmailTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.ForeignKey(MailFollowers, models.DO_NOTHING)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailGroup(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    public = models.CharField(max_length=-1)
    image_medium = models.BinaryField(blank=True, null=True)
    image_small = models.BinaryField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mail_group'


class MailGroupResGroupRel(models.Model):
    mail_group = models.ForeignKey(MailGroup, models.DO_NOTHING)
    groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_group_res_group_rel'
        unique_together = (('mail_group', 'groups'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    notification = models.NullBooleanField()
    auto_delete = models.NullBooleanField()
    body_html = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    model = models.CharField(max_length=128, blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    no_auto_thread = models.NullBooleanField()
    date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=12, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageResPartnerRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    default = models.NullBooleanField()
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    relation_field = models.CharField(max_length=-1, blank=True, null=True)
    hidden = models.NullBooleanField()
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailNotification(models.Model):
    is_read = models.NullBooleanField()
    starred = models.NullBooleanField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_notification'


class MailVote(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_vote'
        unique_together = (('message', 'user'),)


class MailWizardInvite(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    send_mail = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.ForeignKey(MailWizardInvite, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MakeProcurement(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    date_planned = models.DateField()
    qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'make_procurement'


class MessageAttachmentRel(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class MultiCompanyDefault(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    object = models.ForeignKey(IrModel, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company_dest = models.ForeignKey('ResCompany', models.DO_NOTHING)
    expression = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'multi_company_default'


class OsvMemoryAutovacuum(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osv_memory_autovacuum'


class PaymentAcquirer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    website_published = models.NullBooleanField()
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    fees_active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    post_msg = models.TextField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    view_template = models.ForeignKey(IrUiView, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    validation = models.CharField(max_length=-1, blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    environment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer'


class PaymentTransaction(models.Model):
    state_message = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date_create = models.DateTimeField()
    acquirer = models.ForeignKey(PaymentAcquirer, models.DO_NOTHING)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    partner_reference = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    acquirer_reference = models.CharField(max_length=-1, blank=True, null=True)
    partner_address = models.CharField(max_length=-1, blank=True, null=True)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_lang = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_zip = models.CharField(max_length=-1, blank=True, null=True)
    currency_id = models.IntegerField()
    date_validate = models.DateTimeField(blank=True, null=True)
    partner_city = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PlineTaxRel(models.Model):
    pos_line = models.ForeignKey('PosOrderLine', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pline_tax_rel'
        unique_together = (('pos_line', 'tax'),)


class PortalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    portal = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=240, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    in_portal = models.NullBooleanField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class PosCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    image_medium = models.BinaryField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    image_small = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_category'


class PosConfig(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    iface_big_scrollbars = models.NullBooleanField()
    stock_location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    iface_self_checkout = models.NullBooleanField()
    iface_electronic_scale = models.NullBooleanField()
    proxy_ip = models.CharField(max_length=45, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    iface_scan_via_proxy = models.NullBooleanField()
    state = models.CharField(max_length=-1)
    group_by = models.NullBooleanField()
    iface_invoicing = models.NullBooleanField()
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING)
    barcode_discount = models.CharField(max_length=64, blank=True, null=True)
    iface_vkeyboard = models.NullBooleanField()
    barcode_customer = models.CharField(max_length=64, blank=True, null=True)
    barcode_price = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    barcode_weight = models.CharField(max_length=64, blank=True, null=True)
    iface_payment_terminal = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    receipt_header = models.TextField(blank=True, null=True)
    iface_cashdrawer = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    receipt_footer = models.TextField(blank=True, null=True)
    iface_print_via_proxy = models.NullBooleanField()
    barcode_cashier = models.CharField(max_length=64, blank=True, null=True)
    barcode_product = models.CharField(max_length=64, blank=True, null=True)
    discount_pc = models.FloatField(blank=True, null=True)
    discount_product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    display_price_with_taxes = models.NullBooleanField()
    logo = models.BinaryField(blank=True, null=True)
    receipt_use_logo = models.NullBooleanField()
    iface_splitbill = models.NullBooleanField()
    iface_printbill = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pos_config'


class PosConfigJournalRel(models.Model):
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_journal_rel'
        unique_together = (('pos_config', 'journal'),)


class PosConfigPrinterRel(models.Model):
    config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    printer = models.ForeignKey('RestaurantPrinter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_config_printer_rel'
        unique_together = (('config', 'printer'),)


class PosConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_confirm'


class PosDetails(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateField()
    date_start = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_details'


class PosDetailsReportUserRel(models.Model):
    user = models.ForeignKey(PosDetails, models.DO_NOTHING)
    wizard = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_details_report_user_rel'
        unique_together = (('user', 'wizard'),)


class PosDiscount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_discount'


class PosEanWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ean13_pattern = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'pos_ean_wizard'


class PosMakePayment(models.Model):
    payment_date = models.DateField()
    payment_name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_make_payment'


class PosOpenStatement(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_open_statement'


class PosOrder(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sale_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, db_column='sale_journal', blank=True, null=True)
    pos_reference = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, db_column='account_move', blank=True, null=True)
    date_order = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    nb_print = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    sales_person = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='sales_person', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_order'


class PosOrderLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    notice = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    order = models.ForeignKey(PosOrder, models.DO_NOTHING, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    price_subtotal_incl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pos_order_line'


class PosOrderTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='tax', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    pos_order = models.ForeignKey(PosOrder, models.DO_NOTHING, db_column='pos_order', blank=True, null=True)
    base = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_order_tax'


class PosSession(models.Model):
    config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    cash_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    cash_register = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    login_number = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    start_at = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    stop_at = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_session'


class PosSessionOpening(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    pos_session = models.ForeignKey(PosSession, models.DO_NOTHING, blank=True, null=True)
    show_config = models.NullBooleanField()
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING)
    pos_state_str = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_session_opening'


class PricelistPartnerinfo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    suppinfo = models.ForeignKey('ProductSupplierinfo', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    min_quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pricelist_partnerinfo'


class PrinterCategoryRel(models.Model):
    printer = models.ForeignKey('RestaurantPrinter', models.DO_NOTHING)
    category = models.ForeignKey(PosCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'printer_category_rel'
        unique_together = (('printer', 'category'),)


class PrintingAction(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'printing_action'


class PrintingPrinter(models.Model):
    status = models.CharField(max_length=-1)
    system_name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    default = models.NullBooleanField()
    uri = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    status_message = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printing_printer'


class PrintingPrinterUpdateWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printing_printer_update_wizard'


class PrintingReportXmlAction(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    printer = models.ForeignKey(PrintingPrinter, models.DO_NOTHING, blank=True, null=True)
    report = models.ForeignKey(IrActReportXml, models.DO_NOTHING)
    printer_tray = models.ForeignKey('PrintingTray', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printing_report_xml_action'


class PrintingTray(models.Model):
    system_name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    printer = models.ForeignKey(PrintingPrinter, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'printing_tray'


class ProcurementGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    move_type = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProcurementOrder(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, db_column='product_uom')
    product_uos_qty = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uos = models.ForeignKey('ProductUom', models.DO_NOTHING, db_column='product_uos', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    priority = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    date_planned = models.DateTimeField()
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    move_dest = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    partner_dest = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    invoice_state = models.CharField(max_length=-1, blank=True, null=True)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_order'


class ProcurementOrderComputeAll(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_order_compute_all'


class ProcurementOrderpointCompute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_orderpoint_compute'


class ProcurementRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    action = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    group_propagation_option = models.CharField(max_length=-1, blank=True, null=True)
    partner_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    propagate = models.NullBooleanField()
    procure_method = models.CharField(max_length=-1)
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    invoice_state = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_rule'


class ProductAttribute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_line'


class ProductAttributeLineProductAttributeValueRel(models.Model):
    line = models.ForeignKey(ProductAttributeLine, models.DO_NOTHING)
    val = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_line_product_attribute_value_rel'
        unique_together = (('line', 'val'),)


class ProductAttributePrice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    value = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_price'


class ProductAttributeValue(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductProductRel(models.Model):
    att = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING)
    prod = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_product_rel'
        unique_together = (('att', 'prod'),)


class ProductCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductPackaging(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    rows = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    ean = models.CharField(max_length=14, blank=True, null=True)
    ul_qty = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    ul = models.ForeignKey('ProductUl', models.DO_NOTHING, db_column='ul')
    code = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ul_container = models.ForeignKey('ProductUl', models.DO_NOTHING, db_column='ul_container', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPriceHistory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    datetime = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_history'


class ProductPriceList(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_list = models.ForeignKey('ProductPricelist', models.DO_NOTHING, db_column='price_list')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    qty1 = models.IntegerField(blank=True, null=True)
    qty2 = models.IntegerField(blank=True, null=True)
    qty3 = models.IntegerField(blank=True, null=True)
    qty4 = models.IntegerField(blank=True, null=True)
    qty5 = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_list'


class ProductPriceType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField()
    field = models.CharField(max_length=32)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'product_price_type'


class ProductPricelist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField()
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    base = models.IntegerField()
    base_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True)
    price_version = models.ForeignKey('ProductPricelistVersion', models.DO_NOTHING)
    min_quantity = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductPricelistType(models.Model):
    key = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_type'


class ProductPricelistVersion(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    date_end = models.DateField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_version'


class ProductProduct(models.Model):
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    name_template = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    image_variant = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductPutaway(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'product_putaway'


class ProductRemoval(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductSupplierTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    product_code = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.ForeignKey('ResPartner', models.DO_NOTHING, db_column='name')
    sequence = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    delay = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    min_qty = models.FloatField()
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    warranty = models.FloatField(blank=True, null=True)
    uos = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    mes_type = models.CharField(max_length=-1, blank=True, null=True)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    description_purchase = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uos_coeff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    sale_ok = models.NullBooleanField()
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    product_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='product_manager', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    uom_po = models.ForeignKey('ProductUom', models.DO_NOTHING)
    description_sale = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    weight_net = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    rental = models.NullBooleanField()
    image_medium = models.BinaryField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    image_small = models.BinaryField(blank=True, null=True)
    track_all = models.NullBooleanField()
    track_outgoing = models.NullBooleanField()
    loc_rack = models.CharField(max_length=16, blank=True, null=True)
    loc_case = models.CharField(max_length=16, blank=True, null=True)
    track_incoming = models.NullBooleanField()
    loc_row = models.CharField(max_length=16, blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    check_no_negative = models.NullBooleanField()
    lot_unique_ok = models.NullBooleanField()
    purchase_ok = models.NullBooleanField()
    pos_categ_id = models.IntegerField(blank=True, null=True)
    income_pdt = models.NullBooleanField()
    to_weight = models.NullBooleanField()
    expense_pdt = models.NullBooleanField()
    available_in_pos = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductUl(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'product_ul'


class ProductUom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    uom_type = models.CharField(max_length=-1)
    category = models.ForeignKey('ProductUomCateg', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_uom'


class ProductUomCateg(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_uom_categ'


class ProjectAccountAnalyticLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_account_analytic_line'


class PublisherWarrantyContract(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher_warranty_contract'


class PurchaseConfigSettings(models.Model):
    group_uom = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    module_purchase_analytic_plans = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    module_stock_dropshipping = models.NullBooleanField()
    group_costing_method = models.NullBooleanField()
    group_purchase_pricelist = models.NullBooleanField()
    module_purchase_requisition = models.NullBooleanField()
    group_advance_purchase_requisition = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_purchase_double_validation = models.NullBooleanField()
    group_analytic_account_for_purchases = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    default_invoice_method = models.CharField(max_length=-1)
    module_warning = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'purchase_config_settings'


class PurchaseInvoiceRel(models.Model):
    purchase = models.ForeignKey('PurchaseOrder', models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_invoice_rel'
        unique_together = (('purchase', 'invoice'),)


class PurchaseOrder(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency_id = models.IntegerField()
    partner_ref = models.CharField(max_length=-1, blank=True, null=True)
    date_order = models.DateTimeField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    dest_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_column='fiscal_position', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    message_last_post = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    bid_validity = models.DateField(blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, blank=True, null=True)
    bid_date = models.DateField(blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date_approve = models.DateField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1)
    notes = models.TextField(blank=True, null=True)
    invoice_method = models.CharField(max_length=-1)
    shipped = models.NullBooleanField()
    validator = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='validator', blank=True, null=True)
    minimum_planned_date = models.DateField(blank=True, null=True)
    related_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'
        unique_together = (('name', 'company'),)


class PurchaseOrderGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_group'


class PurchaseOrderLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    invoiced = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    date_planned = models.DateField()

    class Meta:
        managed = False
        db_table = 'purchase_order_line'


class PurchaseOrderLineInvoice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_line_invoice'


class PurchaseOrderLineInvoiceRel(models.Model):
    order_line = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_order_line_invoice_rel'
        unique_together = (('order_line', 'invoice'),)


class PurchaseOrderTaxe(models.Model):
    ord = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_order_taxe'
        unique_together = (('ord', 'tax'),)


class ReconcileAccountRel(models.Model):
    reconcile = models.ForeignKey(AccountAutomaticReconcile, models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reconcile_account_rel'
        unique_together = (('reconcile', 'account'),)


class RelModulesLangexport(models.Model):
    wiz = models.ForeignKey(BaseLanguageExport, models.DO_NOTHING)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    action = models.ForeignKey(IrActServer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class Report(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class ReportPaperformat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    format = models.CharField(max_length=-1, blank=True, null=True)
    default = models.NullBooleanField()
    header_line = models.NullBooleanField()
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    margin_right = models.IntegerField(blank=True, null=True)
    margin_top = models.IntegerField(blank=True, null=True)
    margin_left = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    margin_bottom = models.IntegerField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    email = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    fax = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    zip = models.CharField(max_length=24, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country', blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    bic = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state', blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency_id = models.IntegerField()
    rml_footer = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    rml_header = models.TextField()
    rml_paper_format = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    font = models.ForeignKey('ResFont', models.DO_NOTHING, db_column='font', blank=True, null=True)
    account_no = models.CharField(max_length=-1, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    custom_footer = models.NullBooleanField()
    phone = models.CharField(max_length=64, blank=True, null=True)
    rml_header2 = models.TextField()
    rml_header3 = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    rml_header1 = models.CharField(max_length=-1, blank=True, null=True)
    company_registry = models.CharField(max_length=64, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expects_chart_of_accounts = models.NullBooleanField()
    paypal_account = models.CharField(max_length=128, blank=True, null=True)
    overdue_msg = models.TextField(blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    propagation_minimum_delta = models.IntegerField(blank=True, null=True)
    po_lead = models.FloatField()
    sale_note = models.TextField(blank=True, null=True)
    security_lead = models.FloatField()

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.ForeignKey(ResCompany, models.DO_NOTHING, db_column='cid')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    image = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'


class ResCurrencyRate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.DateTimeField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'


class ResFont(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    family = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    mode = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'res_font'
        unique_together = (('family', 'name'),)


class ResGroups(models.Model):
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    share = models.NullBooleanField()
    is_portal = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsActionRel(models.Model):
    uid = models.ForeignKey(IrActionsTodo, models.DO_NOTHING, db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_action_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    code = models.CharField(unique=True, max_length=16)
    date_format = models.CharField(max_length=-1)
    direction = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    thousands_sep = models.CharField(max_length=-1, blank=True, null=True)
    translatable = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    time_format = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    decimal_point = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    iso_code = models.CharField(max_length=16, blank=True, null=True)
    grouping = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=-1)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    image_small = models.BinaryField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    display_name = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    function = models.CharField(max_length=-1, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    supplier = models.NullBooleanField()
    ref = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    is_company = models.NullBooleanField()
    website = models.CharField(max_length=-1, blank=True, null=True)
    customer = models.NullBooleanField()
    fax = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    employee = models.NullBooleanField()
    credit_limit = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    tz = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    image_medium = models.BinaryField(blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    use_parent_address = models.NullBooleanField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    birthdate = models.CharField(max_length=-1, blank=True, null=True)
    vat = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    notify_email = models.CharField(max_length=-1)
    message_last_post = models.DateTimeField(blank=True, null=True)
    opt_out = models.NullBooleanField()
    section = models.ForeignKey(CrmCaseSection, models.DO_NOTHING, blank=True, null=True)
    signup_type = models.CharField(max_length=-1, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    signup_token = models.CharField(max_length=-1, blank=True, null=True)
    last_reconciliation_date = models.DateTimeField(blank=True, null=True)
    vat_subjected = models.NullBooleanField()
    debit_limit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerBank(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    owner_name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    footer = models.NullBooleanField()
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    bank_name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    street = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    state_0 = models.ForeignKey(ResCountryState, models.DO_NOTHING, db_column='state_id', blank=True, null=True)  # Field renamed because of name conflict.
    bank_bic = models.CharField(max_length=16, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, db_column='bank', blank=True, null=True)
    acc_number = models.CharField(max_length=64)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'


class ResPartnerBankType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    format_layout = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank_type'


class ResPartnerBankTypeField(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    required = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    readonly = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    bank_type = models.ForeignKey(ResPartnerBankType, models.DO_NOTHING)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank_type_field'


class ResPartnerCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.ForeignKey(ResPartnerCategory, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    domain = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    shortcut = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResRequestLink(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    object = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_request_link'


class ResUsers(models.Model):
    active = models.NullBooleanField()
    login = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    login_date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    password_crypt = models.CharField(max_length=-1, blank=True, null=True)
    printing_action = models.CharField(max_length=-1, blank=True, null=True)
    printing_printer = models.ForeignKey(PrintingPrinter, models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    display_groups_suggestions = models.NullBooleanField()
    printer_tray = models.ForeignKey(PrintingTray, models.DO_NOTHING, blank=True, null=True)
    default_section = models.ForeignKey(CrmCaseSection, models.DO_NOTHING, blank=True, null=True)
    share = models.NullBooleanField()
    ean13 = models.CharField(max_length=13, blank=True, null=True)
    pos_config = models.ForeignKey(PosConfig, models.DO_NOTHING, db_column='pos_config', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class RestaurantPrinter(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=32)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    proxy_ip = models.CharField(max_length=32, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant_printer'


class RuleGroupRel(models.Model):
    rule_group = models.ForeignKey(IrRule, models.DO_NOTHING)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    advance_payment_method = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    qtty = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleConfigSettings(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    module_web_linkedin = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_sale = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    module_crm = models.NullBooleanField()
    module_mass_mailing = models.NullBooleanField()
    group_multi_salesteams = models.NullBooleanField()
    module_sale_stock = models.NullBooleanField()
    module_account_analytic_analysis = models.NullBooleanField()
    group_sale_pricelist = models.NullBooleanField()
    module_sale_journal = models.NullBooleanField()
    module_website_quote = models.NullBooleanField()
    group_discount_per_so_line = models.NullBooleanField()
    timesheet = models.NullBooleanField()
    group_invoice_so_lines = models.NullBooleanField()
    module_sale_margin = models.NullBooleanField()
    group_uom = models.NullBooleanField()
    module_project = models.NullBooleanField()
    group_sale_delivery_address = models.NullBooleanField()
    module_analytic_user_function = models.NullBooleanField()
    module_warning = models.NullBooleanField()
    time_unit = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='time_unit', blank=True, null=True)
    module_sale_service = models.NullBooleanField()
    module_delivery = models.NullBooleanField()
    group_invoice_deli_orders = models.NullBooleanField()
    task_work = models.NullBooleanField()
    group_mrp_properties = models.NullBooleanField()
    group_route_so_lines = models.NullBooleanField()
    default_picking_policy = models.NullBooleanField()
    default_order_policy = models.CharField(max_length=-1, blank=True, null=True)
    module_project_timesheet = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sale_config_settings'


class SaleMakeInvoice(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    grouped = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_make_invoice'


class SaleMemberRel(models.Model):
    section = models.ForeignKey(CrmCaseSection, models.DO_NOTHING)
    member = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_member_rel'
        unique_together = (('section', 'member'),)


class SaleOrder(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    client_order_ref = models.CharField(max_length=-1, blank=True, null=True)
    date_order = models.DateTimeField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    procurement_group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_column='fiscal_position', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, db_column='payment_term', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    section = models.ForeignKey(CrmCaseSection, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_invoice = models.ForeignKey(ResPartner, models.DO_NOTHING)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    date_confirm = models.DateField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    project = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    partner_shipping = models.ForeignKey(ResPartner, models.DO_NOTHING)
    order_policy = models.CharField(max_length=-1)
    picking_policy = models.CharField(max_length=-1)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, db_column='incoterm', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    shipped = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sale_order'
        unique_together = (('name', 'company'),)


class SaleOrderInvoiceRel(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_invoice_rel'
        unique_together = (('order', 'invoice'),)


class SaleOrderLine(models.Model):
    product_uos_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    sequence = models.IntegerField(blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_uos = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uos', blank=True, null=True)
    invoiced = models.NullBooleanField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    delay = models.FloatField()
    state = models.CharField(max_length=-1)
    order_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    salesman = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    th_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    address_allotment = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('order_line', 'invoice'),)


class SaleOrderLineMakeInvoice(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line_make_invoice'


class SaleOrderTax(models.Model):
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tax'
        unique_together = (('order_line', 'tax'),)


class ShareWizard(models.Model):
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_2 = models.CharField(max_length=64, blank=True, null=True)
    email_3 = models.CharField(max_length=64, blank=True, null=True)
    email_1 = models.CharField(max_length=64, blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    embed_option_title = models.NullBooleanField()
    new_users = models.TextField(blank=True, null=True)
    access_mode = models.CharField(max_length=-1)
    action = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    invite = models.NullBooleanField()
    view_type = models.CharField(max_length=-1)
    embed_option_search = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'share_wizard'


class ShareWizardResGroupRel(models.Model):
    share = models.ForeignKey(ShareWizard, models.DO_NOTHING)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'share_wizard_res_group_rel'
        unique_together = (('share', 'group'),)


class ShareWizardResUserRel(models.Model):
    share = models.ForeignKey(ShareWizard, models.DO_NOTHING)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'share_wizard_res_user_rel'
        unique_together = (('share', 'user'),)


class ShareWizardResultLine(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    newly_created = models.NullBooleanField()
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    password = models.CharField(max_length=64, blank=True, null=True)
    share_wizard = models.ForeignKey(ShareWizard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'share_wizard_result_line'


class StockChangeProductQty(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockChangeStandardPrice(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    new_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_standard_price'


class StockConfigSettings(models.Model):
    group_uom = models.NullBooleanField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    module_procurement_jit = models.NullBooleanField()
    group_stock_packaging = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    module_claim_from_delivery = models.NullBooleanField()
    group_stock_multiple_locations = models.NullBooleanField()
    module_stock_picking_wave = models.NullBooleanField()
    decimal_precision = models.IntegerField(blank=True, null=True)
    module_product_expiry = models.NullBooleanField()
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    group_stock_adv_location = models.NullBooleanField()
    group_stock_tracking_lot = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    group_stock_production_lot = models.NullBooleanField()
    module_stock_dropshipping = models.NullBooleanField()
    group_stock_tracking_owner = models.NullBooleanField()
    group_uos = models.NullBooleanField()
    module_stock_landed_costs = models.NullBooleanField()
    group_stock_inventory_valuation = models.NullBooleanField()
    module_stock_invoice_directly = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_config_settings'


class StockFixedPutawayStrat(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    putaway = models.ForeignKey(ProductPutaway, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fixed_location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_fixed_putaway_strat'


class StockIncoterms(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_incoterms'


class StockInventory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    filter = models.CharField(max_length=-1)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory'


class StockInventoryLine(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    prodlot_name = models.CharField(max_length=-1, blank=True, null=True)
    product_name = models.CharField(max_length=-1, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    prod_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    location_name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    theoretical_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING)
    product_code = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_line'


class StockInvoiceOnshipping(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal_type = models.CharField(max_length=-1, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_invoice_onshipping'


class StockLocation(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    putaway_strategy = models.ForeignKey(ProductPutaway, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    removal_strategy = models.ForeignKey(ProductRemoval, models.DO_NOTHING, blank=True, null=True)
    scrap_location = models.NullBooleanField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    usage = models.CharField(max_length=-1)
    loc_barcode = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    valuation_in_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    valuation_out_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('loc_barcode', 'company'),)


class StockLocationPath(models.Model):
    location_from = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    auto = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    propagate = models.NullBooleanField()
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    invoice_state = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location_path'


class StockLocationRoute(models.Model):
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    warehouse_selectable = models.NullBooleanField()
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    product_selectable = models.NullBooleanField()
    product_categ_selectable = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sale_selectable = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_categ'
        unique_together = (('categ', 'route'),)


class StockLocationRouteMove(models.Model):
    move = models.ForeignKey('StockMove', models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRouteProcurement(models.Model):
    procurement = models.ForeignKey(ProcurementOrder, models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_location_route_procurement'
        unique_together = (('procurement', 'route'),)


class StockMove(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    product_uos_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    move_dest = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    price_unit = models.FloatField(blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    date = models.DateTimeField()
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uos = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uos', blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    date_expected = models.DateTimeField()
    procurement = models.ForeignKey(ProcurementOrder, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey(StockInventory, models.DO_NOTHING, blank=True, null=True)
    partially_available = models.NullBooleanField()
    propagate = models.NullBooleanField()
    restrict_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    procure_method = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    split_from = models.ForeignKey('self', models.DO_NOTHING, db_column='split_from', blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    push_rule = models.ForeignKey(StockLocationPath, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True)
    invoice_state = models.CharField(max_length=-1)
    purchase_line = models.ForeignKey(PurchaseOrderLine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveOperationLink(models.Model):
    reserved_quant = models.ForeignKey('StockQuant', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    operation = models.ForeignKey('StockPackOperation', models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_operation_link'


class StockMoveScrap(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, db_column='product_uom')
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_scrap'


class StockPackOperation(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    processed = models.CharField(max_length=-1)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_pack_operation'


class StockPicking(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=-1)
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    move_type = models.CharField(max_length=-1)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    min_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    recompute_pack_op = models.NullBooleanField()
    max_date = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    invoice_state = models.CharField(max_length=-1)
    reception_to_invoice = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingType(models.Model):
    code = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    default_location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    sequence_0 = models.ForeignKey(IrSequence, models.DO_NOTHING, db_column='sequence_id')  # Field renamed because of name conflict.
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    default_location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockProductionLot(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    last_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_production_lot'
        unique_together = (('name', 'ref', 'product'),)


class StockQuant(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    qty = models.FloatField()
    propagated_from = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    reservation = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    packaging_type = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    negative_move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantMoveRel(models.Model):
    quant = models.ForeignKey(StockQuant, models.DO_NOTHING)
    move = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_move_rel'
        unique_together = (('quant', 'move'),)


class StockQuantPackage(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    ul = models.ForeignKey(ProductUl, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockReturnPicking(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    move_dest_exists = models.NullBooleanField()
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    invoice_state = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wizard = models.ForeignKey(StockReturnPicking, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    product = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('product', 'route'),)


class StockRouteWarehouse(models.Model):
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('warehouse', 'route'),)


class StockTransferDetails(models.Model):
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_transfer_details'


class StockTransferDetailsItems(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sourceloc = models.ForeignKey(StockLocation, models.DO_NOTHING)
    destinationloc = models.ForeignKey(StockLocation, models.DO_NOTHING)
    result_package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey(ProductUom, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True)
    packop = models.ForeignKey(StockPackOperation, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    transfer = models.ForeignKey(StockTransferDetails, models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey(StockProductionLot, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_transfer_details_items'


class StockWarehouse(models.Model):
    crossdock_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    lot_stock = models.ForeignKey(StockLocation, models.DO_NOTHING)
    wh_pack_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    pick_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=5)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    mto_pull = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True)
    reception_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    wh_input_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    delivery_steps = models.CharField(max_length=-1)
    default_resupply_wh = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    wh_qc_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    reception_steps = models.CharField(max_length=-1)
    resupply_from_wh = models.NullBooleanField()
    pack_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    delivery_route = models.ForeignKey(StockLocationRoute, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    in_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    out_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    int_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    buy_pull = models.ForeignKey(ProcurementRule, models.DO_NOTHING, blank=True, null=True)
    buy_to_resupply = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('name', 'company'), ('code', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    logic = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    supplier_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class TempRange(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_range'


class ValidateAccountMove(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class ValidateAccountMoveLines(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move_lines'


class WebShortcut(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_shortcut'
        unique_together = (('menu', 'user'),)


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'


class WizardMultiChartsAccounts(models.Model):
    only_one_chart_template = models.NullBooleanField()
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    code_digits = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    sale_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='sale_tax', blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    purchase_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='purchase_tax', blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_multi_charts_accounts'


class WizardValidateAccountMoveJournal(models.Model):
    wizard = models.ForeignKey(ValidateAccountMove, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wizard_validate_account_move_journal'
        unique_together = (('wizard', 'journal'),)


class WizardValidateAccountMovePeriod(models.Model):
    wizard = models.ForeignKey(ValidateAccountMove, models.DO_NOTHING)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wizard_validate_account_move_period'
        unique_together = (('wizard', 'period'),)


class WizardValuationHistory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    choose_date = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'wizard_valuation_history'


class Wkf(models.Model):
    name = models.CharField(max_length=-1)
    osv = models.CharField(max_length=-1)
    on_create = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf'


class WkfActivity(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    kind = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    join_mode = models.CharField(max_length=3)
    flow_stop = models.NullBooleanField()
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    subflow = models.ForeignKey(Wkf, models.DO_NOTHING, blank=True, null=True)
    split_mode = models.CharField(max_length=3)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    wkf = models.ForeignKey(Wkf, models.DO_NOTHING)
    signal_send = models.CharField(max_length=-1, blank=True, null=True)
    flow_start = models.NullBooleanField()
    action_0 = models.ForeignKey(IrActServer, models.DO_NOTHING, db_column='action_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'wkf_activity'


class WkfInstance(models.Model):
    res_type = models.CharField(max_length=-1, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    wkf = models.ForeignKey(Wkf, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_instance'


class WkfTransition(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    trigger_model = models.CharField(max_length=-1, blank=True, null=True)
    signal = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    act_from = models.ForeignKey(WkfActivity, models.DO_NOTHING, db_column='act_from')
    condition = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    trigger_expr_id = models.CharField(max_length=-1, blank=True, null=True)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING, blank=True, null=True)
    act_to = models.ForeignKey(WkfActivity, models.DO_NOTHING, db_column='act_to')

    class Meta:
        managed = False
        db_table = 'wkf_transition'


class WkfTriggers(models.Model):
    instance = models.ForeignKey(WkfInstance, models.DO_NOTHING, blank=True, null=True)
    workitem = models.ForeignKey('WkfWorkitem', models.DO_NOTHING)
    model = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_triggers'


class WkfWitmTrans(models.Model):
    inst = models.ForeignKey(WkfInstance, models.DO_NOTHING)
    trans = models.ForeignKey(WkfTransition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wkf_witm_trans'
        unique_together = (('inst', 'trans'),)


class WkfWorkitem(models.Model):
    act = models.ForeignKey(WkfActivity, models.DO_NOTHING)
    inst = models.ForeignKey(WkfInstance, models.DO_NOTHING)
    subflow = models.ForeignKey(WkfInstance, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_workitem'
        
class IrFilters(models.Model):
    model_id = models.CharField(max_length=-1)
    domain = models.TextField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    is_default = models.NullBooleanField()
    context = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'ir_filters'
        
class ResCurrency(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    symbol = models.CharField(max_length=4, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    base = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    position = models.CharField(max_length=-1, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'res_currency'
