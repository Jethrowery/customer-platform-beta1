from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils.functional import cached_property

# Create your models here.



class Entity(models.Model):
    # alphanumeric = RegexValidator(
        # r'^[A-Z0-9]*$', 'Only alphanumeric characters are allowed.')
    
    entityname = models.CharField(max_length=225, blank=True)
    entitynumber = models.CharField(max_length=8, blank=True,
                            null=True)

    def __str__(self):
        return self.entityname
    

class ParentEntity(models.Model):
    
    entitynumber = models.ForeignKey(
        Entity, on_delete=models.PROTECT, max_length=8, default=None, blank=True, related_name='entity_no')
    parententity_no = models.ForeignKey(
        Entity, on_delete=models.PROTECT, max_length=8, default=None, blank=True, related_name='parent_no')

    def __str__(self):
        return self.entitynumber

class ChartOfAccounts(models.Model):
    
    dr_cr = (
        ('dr', 'Dr'),
        ('cr', 'Cr'),
    )

    category = (
        ('on_balance_sheet', 'On_balance_sheet'),
        ('off_balance_sheet', 'Off_balance_sheet'),
    )
    
    accountno = models.CharField(max_length=15, blank=False, default=None,)
    accountname = models.CharField(max_length=100, blank=False, default=None,)
    subledger_no = models.CharField(max_length=25, blank=False, default=None,)
    subname = models.CharField(max_length=100, blank=False, default=None,)
    description = models.TextField(max_length=225, blank=False, default=None,)
    category = models.CharField(max_length=100, choices=category, default=None)
    side = models.CharField(max_length=3, choices=dr_cr, default=None)

    def __str__(self):
        return str(self.accountname)

class SubLedger(models.Model):

    dr_cr = (
        ('dr', 'Dr'),
        ('cr', 'Cr'),
    )
    
    entitynumber = models.ForeignKey(
        Entity, on_delete=models.PROTECT, max_length=6, default=None, blank=True, related_name='subledgerentityno')
    subname = models.ForeignKey(
        ChartOfAccounts, on_delete=models.PROTECT, blank=False, default=None, related_name='subledgername')
    subledger_no = models.ForeignKey(
        ChartOfAccounts, on_delete=models.PROTECT, blank=False, default=None, related_name='subledgernumber')
    side = models.ForeignKey(
        ChartOfAccounts, on_delete=models.PROTECT, default=None, related_name='subledgerside')
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    entrydate = models.DateTimeField(default=timezone.now)
    value_date = models.DateField(
        "Entry date dd/mm/yyyy", auto_now_add=False, auto_now=False, blank=True, default=None, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=None, related_name='subledgerUser')
    export_to_csv = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-value_date',)

    def __str__(self):
        return self.subname



class Accounts(models.Model):

    entitynumber = models.OneToOneField(
        Entity, on_delete=models.PROTECT, default=None, blank=True, related_name='no_entity')
    accountno = models.OneToOneField(
        ChartOfAccounts, on_delete=models.PROTECT, default=None, blank=False, related_name='acctno')
    accountname = models.OneToOneField(
        ChartOfAccounts, on_delete=models.PROTECT, blank=False, default = None, related_name='acctname')
    #image = models.ImageField(
    #    _("Image"), upload_to=upload_to, default='posts/default.jpg')
    category = models.OneToOneField(
        ChartOfAccounts, on_delete=models.PROTECT, blank=False, default = None, related_name='acctcat')
    content = models.TextField()
    slug = models.SlugField(max_length=250, default=None)#, unique_for_date='published')
    #finalizeddate = models.DateTimeField(default=timezone.now)
    value_date = models.DateField("Entry date dd/mm/yyyy", auto_now_add=False, auto_now=False, blank=True, null=False)
    side = models.ForeignKey(
        ChartOfAccounts, on_delete=models.PROTECT, max_length=3, default=None, related_name='acctside')
    amount = models.DecimalField(
        max_digits=100, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, related_name='maps')
    export_to_csv = models.BooleanField(default=True)

    class Meta:
        ordering = ('-value_date',)

    def __str__(self):
        return str(self.accountname)

class AnnualReports(models.Model):
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    class AccountsStatus(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')


    accttype = (
        ('interim', 'Interim'),
        ('year-end', 'Year-end'),
    )
    
    auditors = (
        ('pwc', 'PWC'),
        ('kpmg', 'KPMG'),
        ('deloittes', 'Deloittes'),
        ('ey', 'ey'),
        ('bdo', 'bdo'),
        ('grant_thorton', 'Grant_Thorthon'),
    )
    
    reportcat = (
        ('solo', 'Solo'),
        ('group', 'Group'),
    )

    # Example model only
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, default=None)
    status = models.CharField(
        max_length=10, choices=options, default='published')
    accounttype = models.CharField(
        max_length=10, choices=accttype, default='interim')
    auditor = models.CharField(
        max_length=25, choices=auditors, default=None)
    reportcategory = models.CharField(
        max_length=10, choices=reportcat, default='solo')
    category = models.ForeignKey(
        ChartOfAccounts, on_delete=models.PROTECT, blank=False, default=None)
    as_at_date = models.DateField(
        "Entry date dd/mm/yyyy", auto_now_add=False, auto_now=False, blank=True, null=False)
    entitynumber = models.ForeignKey(
        Entity, on_delete=models.PROTECT, max_length=6, default=None, blank=True, related_name="ntitynumber")
    count = models.IntegerField(null=True, default=0)
    objects = models.Manager()  # default manager
    accountsobjects = AccountsStatus()  # custom manager


    def __str__(self):
        return self.title


class DemoTable(models.Model):
    
    #alphanumeric = RegexValidator(
    #    r'^[A-Z0-9]*$', 'Only alphanumeric characters are allowed.')
    
    id = models.IntegerField(blank=True,default=None, primary_key=True,)
    #day = models.CharField(max_length=50, blank=True, default=None, null=True,)
    dealnum = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    dealtype = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    prodcode = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    prodtype = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    currency_code = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    securityname = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    bond_type = models.CharField(max_length=50, blank=True, default=None, null=True,)
    isin_code = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    customer_name = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    buyer_country_code = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    buyer_legal_entity_identifier = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    buyer_market_identifier_code = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    delivery_type = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    classification_of_financial_instruments = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    investment_decision_identifier = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    interest_frequency = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    roll_frequency = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    accrual_or_cash_basis = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    sell_or_purchase = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    portfolio_name = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    business_unit = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    #slug = models.SlugField(max_length=250, default=None)
    interest_rate = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    new_interest_rate = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    interest_due = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    accrual_daily = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    accrual_to_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    net_position = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    book_value = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    current_value = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    market_value = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    purchase_price = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    yield_value = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    maturity_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    original_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    bcu_principal_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    revaluation_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    amortisation_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    bcu_amortisation_amount = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    premium_discount_outst = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    premium_discount_to_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    premium_discount_daily = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    value_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    maturity_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    purchase_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    lia_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    nia_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    lrc_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    nrc_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    accr_daily_from = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    accr_daily_to = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    date_from = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    date_to = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    int_ref = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    hedge_id = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    hedge_percentage = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    option_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    expiry_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    structure_type = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    hd_deal_number = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    review_date = models.CharField(
        max_length=50, blank=True, default=None, null=True,)
    deal_type_group = models.CharField(
        max_length=100, blank=True, default=None, null=True,)
    count = models.IntegerField(default=None, null=True,)
    issue_description = models.CharField(max_length = 100, default=None, null=True,)
    
    
    def __str__(self):
        return self.dealnum
    
    # @cached_property
    # def acounting(self):
    #     return self.dealnum.filter(buyer_country_code='UK').count()
