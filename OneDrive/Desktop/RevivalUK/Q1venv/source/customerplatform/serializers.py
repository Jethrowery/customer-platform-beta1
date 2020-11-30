from django.conf import settings
from .models import Accounts, AnnualReports, SubLedger, DemoTable
from rest_framework import serializers


class SubLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLedger
        fields = ('id', 'slug', 'entitynumber', 'subledger_no ',
                  'subname', 'amount', 'side', 'value_date', 'user')


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id', 'slug', 'entitynumber', 'accountno',
                  'accountname', 'amount', 'side', 'value_date', 'user')


class AnnualReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualReports
        fields = ('title', 'id', 'slug', 'entitynumber', 'status', 'accounttype',
                  'auditor', 'reportcategory', 'as_at_date')


class DemoTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoTable
        fields = ('id', 'customer_name', 'isin_code', 'portfolio_name', 'hd_deal_number', 'buyer_country_code',
                  'buyer_legal_entity_identifier', 'buyer_market_identifier_code', 'currency_code', 'lia_date', 'lrc_date',
                  'classification_of_financial_instruments', 'investment_decision_identifier', 'bond_type', 'maturity_date',
                  'review_date', 'net_position')


# class DemoTableSmallSerializer(serializers.ModelSerializer):
#     description = serializers.CharField()
#     errors = serializers.CharField()

#     class Meta:
#         model = DemoTable
#         fields = ('description', 'errors')


# class PassThroughSerializer(serializers.Field):
#     def to_representation(self, instance):
#         return None

#     def to_internal_value(self, data):
#         return data

class DemoTableErrCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoTable
        fields = ['acounting']
        
    def validate(self, data):
        acounting = data.count("acounting", None)  # pop("acounting",None)
        return super().validate(data)

    def to_representation(self, instance):
        data = super().to_representation (instance)
        data['acounting'] = []#DemoTable.objects.filter(buyer_country_code='UK')
        return data
    
