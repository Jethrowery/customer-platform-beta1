from django.contrib import admin
from .models import SubLedger
from .models import Accounts
from .models import AnnualReports
from .models import ChartOfAccounts
from .models import Entity
from .models import ParentEntity
from .models import DemoTable

# Register your models here.

admin.site.register([SubLedger, Accounts, ChartOfAccounts, AnnualReports, Entity, ParentEntity, DemoTable])
