from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db.models import F
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.views import APIView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.response import Response
from rest_framework import viewsets, filters, generics, permissions
from .serializers import (AccountsSerializer, AnnualReportsSerializer, 
                          SubLedgerSerializer, DemoTableSerializer, DemoTableErrCountSerializer)
from .models import Accounts, AnnualReports, SubLedger, DemoTable
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



codesnap = "SELECT id, customer_name, isin_code, portfolio_name, hd_deal_number As Deal_date, buyer_country_code,buyer_legal_entity_identifier, buyer_market_identifier_code, currency_code, lia_date, lrc_date As Expiry_date, classification_of_financial_instruments, investment_decision_identifier, bond_type, maturity_date, review_date, net_position FROM customerplatform_demotable WHERE "


#class DemoTable_small (generics.ListAPIView):
class DemoTableDetail_small (generics.RetrieveAPIView):

    def get(self, request, format=None):
        serializer = DemoTableErrCountSerializer()
        queryset = DemoTable.objects.filter(buyer_country_code='UK')
        return Response(serializer.data)


#APIView
class DemoTableDetail_err_bcc (generics.RetrieveAPIView):
    #http_method_names = ['get']#, 'head']
    #serializer_class = DemoTableSerializer

    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(buyer_country_code='UK')
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)


class DemoTableDetail_err_bei (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(buyer_legal_entity_identifier__icontains='CUKLVMY') | Q(
                buyer_legal_entity_identifier__icontains='OUKLVMY') | Q(buyer_legal_entity_identifier__icontains='4U9LVMY') | Q(buyer_legal_entity_identifier__icontains='4UKLV0Y'))
        serializer = DemoTableSerializer(queryset, many=True)
        print(request.data)
        return Response(serializer.data)
    
    
    

class DemoTableDetail_err_bmi (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(Q(buyer_market_identifier_code__icontains='DEFS'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

class DemoTableDetail_err_cc (generics.RetrieveAPIView):
    
    def get(self, request, format=None): 
        serializer_class = DemoTableSerializer
        queryset = DemoTable.objects.filter(currency_code='EOR')
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)


class DemoTableDetail_err_isin (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(isin_code__isnull=True)
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)
        
        
class DemoTableDetail_err_mexpiry (generics.RetrieveAPIView):
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(lia_date__isnull=True)
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

class DemoTableDetail_err_iexpiry (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(~Q(
            lia_date=F('lrc_date')) & ~Q(lia_date__isnull=True))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

class DemoTableDetail_err_imaturity (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(maturity_date__isnull=True)
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

class DemoTableDetail_err_transmittingent (generics.RetrieveAPIView):
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(buyer_legal_entity_identifier__icontains='17307') | Q(
                buyer_legal_entity_identifier__icontains='99431'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)


class DemoTableDetail_instmtexpiry (generics.RetrieveAPIView):
    """ inconsistent instrument classification identifier"""
    
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(classification_of_financial_instruments__icontains='LBN0'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)
        
        
class DemoTableDetail_iinstmtexpiry (generics.RetrieveAPIView):
    """incorrect instrument classification identifier"""

    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(classification_of_financial_instruments__icontains='ISLIKK'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)



class DemoTableDetail_idi (generics.RetrieveAPIView):

    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(investment_decision_identifier__icontains='00SC003'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

    
class DemoTableDetail_reviewdate (generics.RetrieveAPIView):
    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(review_date__isnull=True)
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)
    

class DemoTableDetail_netamt (generics.RetrieveAPIView):

    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(
            Q(net_position__icontains='-'))
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)



class DemoTableDetail_missingbond (generics.RetrieveAPIView):

    def get(self, request, format=None):
        queryset = DemoTable.objects.filter(bond_type__isnull=True)
        serializer = DemoTableSerializer(queryset, many=True)
        return Response(serializer.data)

# class DemoTableDetail_err(generics.RetrieveAPIView):

#     serializer_class = AccountsSerializer
#     #LF error fix
#     static_qry = 'DemoTable.objects.raw("SELECT customer_name, isin_code, portfolio_name, hd_deal_number As Deal_date, buyer_country_code,              buyer_legal_entity_identifier, buyer_market_identifier_code, currency_code, lia_date, lrc_date As Expiry_date, classification_of_financial_instruments, investment_decision_identifier, bond_type, maturity_date, review_date, net_position FROM customerplatform_demotable WHERE'
    
#     qry_table = ['buyer_country_code = "UK"', 'buyer_legal_entity_identifier NOT LIKE "%4UKLVMY22DS%"', 'buyer_market_identifier_code NOT LIKE "%XN%"',
#                  'currency_code = "EOR"', 'isin_code ISNULL', 'WHERE lia_date ISNULL', 'lia_date <> lrc_date', 'maturity_date ISNULL', 'classification_of_financial_instruments Like "%LBN0%"', 'classification_of_financial_instruments Like "%ISLIKK%"', 'WHERE investment_decision_identifier Like "%00SC003%"', 'review_date ISNULL', 'net_position Like "%-%"', 'bond_type ISNULL'
#                  ]
    
#     close_off = '”)'
    
#     queryset = DemoTable.objects.filter(buyer_country_code='UK')  # .only()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Accounts, slug=item)



class AccountsList(generics.ListAPIView):

    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()


class AccountsDetail(generics.RetrieveAPIView):

    serializer_class = AccountsSerializer
    #LF error fix
    queryset = Accounts.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Accounts, slug=item)

# Post Search


class AccountListDetailfilter(generics.ListAPIView):

    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']

# Post Admin

# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CreateAccount(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminAccountDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class EditAccount(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()


class DeleteAccount(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountsSerializer
    queryset = Accounts.objects.all()


#####


class SubLedgerList(generics.ListAPIView):

    serializer_class = AccountsSerializer
    queryset = SubLedger.objects.all()


class SubLedgerDetail(generics.RetrieveAPIView):

    serializer_class = AnnualReportsSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Accounts, slug=item)

# Post Search


class SubLedgerListDetailfilter(generics.ListAPIView):

    queryset = SubLedger.objects.all()
    serializer_class = SubLedgerSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']

# Post Admin

# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CreateSubLedger(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = SubLedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminSubLedgerDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SubLedger.objects.all()
    serializer_class = SubLedgerSerializer


class EditSubLedgert(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubLedgerSerializer
    queryset = SubLedger.objects.all()


class DeleteSubLedger(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubLedgerSerializer
    queryset = SubLedger.objects.all()
