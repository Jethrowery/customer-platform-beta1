from .views import AccountsList, AccountsDetail, AccountListDetailfilter, CreateAccount, EditAccount, AdminAccountDetail, DeleteAccount, DemoTableDetail_small, DemoTableDetail_err_bcc, DemoTableDetail_err_bei, DemoTableDetail_err_bmi, DemoTableDetail_err_cc, DemoTableDetail_err_isin, DemoTableDetail_err_mexpiry, DemoTableDetail_err_iexpiry, DemoTableDetail_err_imaturity, DemoTableDetail_err_transmittingent, DemoTableDetail_instmtexpiry, DemoTableDetail_iinstmtexpiry, DemoTableDetail_idi, DemoTableDetail_reviewdate, DemoTableDetail_netamt, DemoTableDetail_missingbond

from django.urls import path

app_name = 'customerplatform'

urlpatterns = [
    path('accountlist/', AccountsList.as_view(), name='listpost'),
    path('account/<str:pk>/', AccountsDetail.as_view(), name='detailsaccount'),
    path('search/', AccountListDetailfilter.as_view(), name='searchaccount'),
    
    # Post Demo URLs
    path('errs_small/', DemoTableDetail_small.as_view(), name='errmain'),
    path('errd_bcc/', DemoTableDetail_err_bcc.as_view(), name='err01'),
    path('errd_bei/', DemoTableDetail_err_bei.as_view(), name='err02'),
    path('errd_bmi/', DemoTableDetail_err_bmi.as_view(), name='err03'),
    path('errd_cc/', DemoTableDetail_err_cc.as_view(), name='err04'),
    path('errd_isin/', DemoTableDetail_err_isin.as_view(), name='err05'),
    path('errd_mexpiry/', DemoTableDetail_err_mexpiry.as_view(), name='err06'),
    path('errd_iexpiry/', DemoTableDetail_err_iexpiry.as_view(), name='err07'),
    path('errd_imaturity/', DemoTableDetail_err_imaturity.as_view(), name='err08'),
    path('errd_transmit/', DemoTableDetail_err_transmittingent.as_view(), name='err09'),
    path('errd_instmtexpiry/', DemoTableDetail_instmtexpiry.as_view(), name='err10'),
    path('errd_iinstmtexpiry/', DemoTableDetail_iinstmtexpiry.as_view(), name='err11'),
    path('errd_idi/', DemoTableDetail_idi.as_view(), name='err12'),
    path('errd_reviewdate/', DemoTableDetail_reviewdate.as_view(), name='err13'),
    path('errd_netamt/', DemoTableDetail_netamt.as_view(), name='err14'),
    path('errd_missingbond/', DemoTableDetail_missingbond.as_view(), name='err15'),
    
    # Post Admin URLs
    path('admin/create/', CreateAccount.as_view(), name='createaccount'),
    path('admin/edit/accountdetail/<int:pk>/',
         AdminAccountDetail.as_view(), name='admindetailaccount'),
    path('admin/edit/<int:pk>/', EditAccount.as_view(), name='editaccount'),
    path('admin/delete/<int:pk>/', DeleteAccount.as_view(), name='deleteaccount'),
]
