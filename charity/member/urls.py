
from django.urls import path, include
from member import views
# from django.conf import settings

app_name = 'member'
 


urlpatterns = [
    path('',views.home, name='home'),
    path('dashboard/',views.home12,name='dashboard'),
    path('dashboard/new_user/<int:pk>',views.UserCreateViewDash.as_view(), name='user'),
    path('dashboard/bitcoin_detail/<int:pk>',views.bitcoin_detail, name='bitcoin_detail'),
    path('dashboard/update/<int:pk>',views.UserUpdateViewDash.as_view(), name='update'),
    path('dashboard/downline/<int:pk>',views.downline_member_list, name='downline_team'),
    path('dashboard/sponsor/<int:pk>',views.DirectSponsorTableView.as_view(), name='direct_sponsor_team'),
    path('dashboard/singleline/<int:pk>',views.SingleLineListTableView.as_view(), name='single_leg'),
    path('dashboard/level_income/<int:pk>', views.level_income, name='level_income'),
    path('dashboard/transfer_balance', views.transfer_balance,name ='transfer_balance'),
    path('dashboard/transfer_balance/<int:pk>', views.transfer_balance,name ='transfer_balance'),
    path('dashboard/activate_account/<int:pk>',views.activate_account, name = 'activate_account'),
    path('dashboard/withdrawal_fund/<int:pk>',views.withdrawal_fund, name = 'withdrawal_fund'),
    path('dashboard/reward_income/<int:pk>', views.reward_income, name = 'reward_income'),
    path('dashboard/withdrawal_report/<int:pk>',views.withdrawal_report,name = 'withdrawal_report'),
    path('gourl_callback.html/', views.callback, name='callback'),
    path('cripto/',views.cryptobox_rendering, name='rendaring'),



#     path('form/',views.RegistrationView.as_view(), name='form_a'),
    # path('update/<int:pk>',views.UpdateViewDash.as_view(), name='update'),
    
#     path('applications/',views.ApplicationListView.as_view(), name='applications'),
    # path('application/',views.UserListTableView.as_view(), name='applicationtable'),
#     path('delete/<int:pk>',views.ApplicationDeleteView.as_view(), name='application_delete'),
#     path('approve/<int:pk>',views.approve_user,name='approve_user'),
#     path('details/<int:pk>',views.ApplicationDetailsView.as_view(), name='details'),
    
    # path('downline/<int:pk>',views.DownlineTeamTableView.as_view(), name='downline_team'),
    # path('sponsor/<int:pk>',views.direct_sponsor, name='direct_sponsor_team'),
    
    # path('singleline/<int:pk>',views.single_line, name='single_leg'),
    
]