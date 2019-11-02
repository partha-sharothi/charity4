from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django_tables2 import SingleTableView
from .forms import UserProfileInfoForm, UserForm, BalanceTransferForm, AccoutActivationForm ,WithdrawalFundForm, BitcoinDetailForm
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo, Activity
# from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .tables import UserInfoTable
from django.urls import reverse, reverse_lazy
from django.views import generic
import absoluteuri
from datetime import timedelta
import pytz

utc=pytz.UTC

# # Create your views here.


def user_activitys(self):
    
    user_is = get_object_or_404(UserProfileInfo, user_profile=self.user)
    downline_number = list(UserProfileInfo.objects.filter(application_date__gt = user_is.application_date, confirm=True).order_by('confirmation_date'))
    direct_users =list(UserProfileInfo.objects.filter(confirm = True, sponsor = user_is ).order_by('confirmation_date'))
    obj=len(list(Activity.objects.filter(user=user_is)))
    # import pdb;pdb.set_trace()
    if len(downline_number)>=2 and len(direct_users)>=1 and obj==0:
        obj = Activity.objects.create()
        obj.level = 1
        obj.user = user_is
        x = downline_number[1]
        date_of_user_20 = x.confirmation_date
        y = direct_users[0]
        date_of_first_user = y.confirmation_date
        if date_of_user_20>date_of_first_user:

            obj.start_date = date_of_user_20                    
        else:
            obj.start_date = date_of_first_user

        obj.end_date = obj.start_date + timedelta(days=1) 
        obj.save()   
            

    elif len(downline_number)>=4 and len(direct_users)>=2 and obj==1:
        pre_obj=get_object_or_404(Activity, level=1, user=user_is)
        pre_obj_end_date = pre_obj.end_date
        obj = Activity.objects.create()
        obj.level = 2
        obj.user = user_is
        x = downline_number[3]
        date_of_user_40 = x.confirmation_date
        y = direct_users[1]
        date_of_first_user = y.confirmation_date
        if date_of_user_40>date_of_first_user and date_of_user_40>pre_obj_end_date :
            obj.start_date = date_of_user_40
        elif date_of_first_user>date_of_user_40 and date_of_first_user>pre_obj_end_date:
            obj.start_date = date_of_first_user
        else:
            obj.start_date = pre_obj_end_date

        obj.end_date = obj.start_date + timedelta(days=1) 
        obj.save()
   

    elif len(downline_number)>=6 and len(direct_users)>=3 and obj==2:
        pre_obj=get_object_or_404(Activity, level=2, user=user_is)
        pre_obj_end_date = pre_obj.end_date
        
        obj = Activity.objects.create()
        obj.level = 3
        obj.user = user_is
        x = downline_number[5]
        date_of_user_100 = x.confirmation_date
        y = direct_users[2]
        date_of_first_user = y.confirmation_date
        if date_of_user_100>date_of_first_user and date_of_user_100>pre_obj_end_date :
            obj.start_date = date_of_user_100
        elif date_of_first_user>date_of_user_100 and date_of_first_user>pre_obj_end_date:
            obj.start_date = date_of_first_user
        else:
            obj.start_date = pre_obj_end_date 

        obj.end_date = obj.start_date + timedelta(days=1) 
        obj.save()

    elif len(downline_number)>=10 and len(direct_users)>=4 and obj==3:
        pre_obj=get_object_or_404(Activity, level=3, user=user_is)
        pre_obj_end_date = pre_obj.end_date

        obj = Activity.objects.create()
        obj.level = 4
        obj.user = user_is
        x = downline_number[9]
        date_of_user_200 = x.confirmation_date
        y = direct_users[3]
        date_of_first_user = y.confirmation_date
        if date_of_user_200>date_of_first_user and date_of_user_200>pre_obj_end_date :
            obj.start_date = date_of_user_200
        elif date_of_first_user>date_of_user_200 and date_of_first_user>pre_obj_end_date:
            obj.start_date = date_of_first_user
        else:
            obj.start_date = pre_obj_end_date

        obj.end_date = obj.start_date + timedelta(days=1) 
        obj.save()

    elif len(downline_number)>=15 and len(direct_users)>=5 and obj==4:
        pre_obj=get_object_or_404(Activity, level=4, user=user_is)
        pre_obj_end_date = pre_obj.end_date

        obj = Activity.objects.create()
        obj.level = 5
        obj.user = user_is
        x = downline_number[14]
        date_of_user_400 = x.confirmation_date
        y = direct_users[4]
        date_of_first_user = y.confirmation_date
        if date_of_user_400>date_of_first_user and date_of_user_400>pre_obj_end_date :
            obj.start_date = date_of_user_400
        elif date_of_first_user>date_of_user_400 and date_of_first_user>pre_obj_end_date:
            obj.start_date = date_of_first_user
        else:
            obj.start_date = pre_obj_end_date

        obj.end_date = obj.start_date + timedelta(days = 1)
        obj.save()
    

    elif len(downline_number)>=24 and len(direct_users)>=6 and obj==5:
        pre_obj=get_object_or_404(Activity, level=5, user=user_is)
        pre_obj_end_date = pre_obj.end_date

        obj = Activity.objects.create()
        obj.level = 6
        obj.user = user_is
        x = downline_number[23]
        date_of_user_18000 = x.confirmation_date
        y = direct_users[14]
        date_of_first_user = y.confirmation_date
        if date_of_user_18000>date_of_first_user and date_of_user_18000>pre_obj_end_date :
            obj.start_date = date_of_user_18000
        elif date_of_first_user>date_of_user_18000 and date_of_first_user>pre_obj_end_date:
            obj.start_date = date_of_first_user
        else:
            obj.start_date = pre_obj_end_date

        obj.end_date = obj.start_date + timedelta(days = 1)
        obj.save()





def home(request):
    return render(request,'index.html')


@login_required
def home12(request):


    # def user_activites(self):
    #     user_is = get_object_or_404(UserProfileInfo, user_profile=self.user)
    #     user_activity_account = Activity.objects.filter(user=user_is)
    #     direct_users =list(UserProfileInfo.objects.filter(confirm = True, sponsor = user_is ).order_by('confirmation_date'))
    #     # import pdb;pdb.set_trace()
    #     # user_activity_account.level.count()
    #     if len(direct_users) <= 18 and user_activity_account.count() < len(direct_users):
    #         i = user_activity_account.count()
    #         x = direct_users.index(direct_users[i])
    #         print(x)
    #         # import pdb;pdb.set_trace()
    #         users_are = direct_users[x:]
    #         x += 1
    #         i=i+1
    #         for user in users_are:
    #             obj = Activity.objects.create()
    #             obj.user = user_is
    #             obj.level = i
    #             # import pdb;pdb.set_trace()
    #             obj.start_date = get_object_or_404(Activity, level= i-1).end_date + timedelta(days=1)
    #             if obj.start_date < user.confirmation_date:
    #                 obj.start_date = user.confirmation_date

    #             obj.end_date = obj.start_date + timedelta(days=7) 
                    
    #             obj.level_status_check()

    #             obj.save()

    #     return None        

    
    
    

########-----------single_leg----start------#####################
    def single_line(request, *args, **kwargs):
        # user_id = kwargs.get('pk')
        user=request.user
        user = get_object_or_404(UserProfileInfo, user_profile=user)
        if user.confirm == True:
            users=UserProfileInfo.objects.filter(confirmation_date__gt = user.confirmation_date)
        
            return users.count()
        return None
    
    single_leg = single_line(request)
########-----------single_leg----end------#####################

############## -------------points------start-----#################

    def downline_team_member(request, *args, **kwargs):
        # user_id = kwargs.get('pk')
        user = request.user.id
        user = get_object_or_404(UserProfileInfo, user_profile=user)
        # member = StaffMember.objects.get(id__id=user_id)

        new_list = [user]

    

        def get_final_team(qs):
            team = []
            staffmembers = UserProfileInfo.objects.filter(sponsor__in=qs, confirm=True)

            team += staffmembers 
            if staffmembers:
                interim_team_qs = get_final_team(staffmembers)
                for qs in interim_team_qs:
                    team.append(qs)
            # else:
            #     team = [qs]

            return team
        new_list = get_final_team(new_list)
        
        numbers = len(new_list)
        # to find the index of user
        # number = new_list.index(user)
    
        return numbers  

    points = downline_team_member(request)*3 


############## -------------points------end-----#################
###############--------->>>>> refferal_bonus<<<<<------>>>>start<<<<<<<<-----########
    
    income = UserProfileInfo.level_bonus(request)
    # request.build_absolute_uri("/media/"+config.MEMBERSHIP_CARD_BACKGROUND)
    id = f"new_user/{request.user.id}"
    referral_url = request.build_absolute_uri(id)

    # user_activites(request)
    user_activitys(request)

    user_id = request.user.id
    user_is = get_object_or_404(UserProfileInfo, id=user_id)
    user_activity = Activity.objects.filter(user=user_is)
    for activity in user_activity:
        activity.level_status_check()

    # import pdb; pdb.set_trace()
###############--------->>>>> refferal_bonus<<<<<------>>>>end<<<<<<<<-----########
    return render(request,'index_dash.html',{'user_activity':user_activity,'referral_url':referral_url, 'single_leg':single_leg,'points':points,'income':income}) 

def bitcoin_detail(request, *args, **kwargs):
    if request.method == "POST":
        form_is = BitcoinDetailForm(data=request.POST)
        if form_is.is_valid():
            
            print(form_is.cleaned_data['bitcoin_address'])
            print(form_is.cleaned_data['otp'])
            return redirect('/')
        
    form = BitcoinDetailForm()

    return render(request, 'bitcoin_detail.html',{'form':form}) 



def downline_member_list(request, *args, **kwargs):
    # user = kwargs.get('pk')
    user_id = request.user
    user = get_object_or_404(UserProfileInfo, user_profile=user_id)
    # k=Application.objects.all()
    # print(k)
    # import pdb;pdb.set_trace()
    name = user
    name1 = list(name.sponsored.filter(confirm=True))
    name2 = [] #Application.objects.none()
    name3 = [] #Application.objects.none()
    name4 = [] #Application.objects.none()
    name5 = [] #Application.objects.none()
    name6 = [] #Application.objects.none()
    name7 = [] #Application.objects.none()
    name8 = [] #Application.objects.none()
    name9 = [] #Application.objects.none()
    name10 = [] #Application.objects.none()
    for x1 in name1:
        name2 += list(x1.sponsored.filter(confirm=True)) 
    for x2 in name2:
        name3 += list(x2.sponsored.filter(confirm=True))
    for x3 in name3:
        name4 += list(x3.sponsored.filter(confirm=True))
    for x4 in name4:
        name5 += list(x4.sponsored.filter(confirm=True)) 
    for x5 in name5:
        name6 += list(x5.sponsored.filter(confirm=True))
    for x6 in name6:
        name7 += list(x6.sponsored.filter(confirm=True))
    for x7 in name7:
        name8 += list(x7.sponsored.filter(confirm=True))
    for x8 in name8:
        name9 += list(x8.sponsored.filter(confirm=True))
    for x9 in name9:
        name10 += list(x9.sponsored.filter(confirm=True))

    names = name1+ name2+name3+name4+name5+name6+name7+name8+name9+name10
                       
    return render(request, 'downline_list.html',{'name1':name1, 'name2':name2, 'name3':name3, 'name4':name4, 'name5':name5,
                                                'name6':name6, 'name7':name7, 'name8':name8, 'name9':name9, 'name10':name10})           



class UserCreateViewDash(generic.View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        # user_id = self.request.user
        profile = get_object_or_404(UserProfileInfo, user_profile=user_id)
        referral_user = get_object_or_404(User, id=profile.id)
        profile_info_form = UserProfileInfoForm()
        user_info_form = UserForm()
        return render(request, 'form.html', {'referral_user': referral_user, 'profile_info_form': profile_info_form, 'user_info_form':user_info_form})

    def post(self, request, *args, **kwargs):
        # user_id = self.request.user
        # sponsor_user = get_object_or_404(UserProfileInfo, user_profile=user_id)
        user_id = kwargs.get('pk')        
        sponsor_user = get_object_or_404(UserProfileInfo, user_profile=user_id)
        # referral_user = get_object_or_404(User, id=profile.id)    
        profile_info_form = UserProfileInfoForm(data=request.POST)
        user_info_form = UserForm(data=request.POST)
        # import pdb;pdb.set_trace()
        print(profile_info_form.is_valid())
        print(user_info_form.is_valid())
        if user_info_form.is_valid() and profile_info_form.is_valid():
            user = user_info_form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            
            profile = profile_info_form.save(commit=False)
            profile.sponsor = sponsor_user
            profile.user_profile = user
            profile.save()
            
            return redirect('/')

        return render(request, 'form.html',{'profile_info_form': profile_info_form, 'user_info_form':user_info_form})



class UserUpdateViewDash(generic.View):

    def get(self, request, *args, **kwargs):
        # user_id = kwargs.get('pk')
        user_id = self.request.user
        profile = get_object_or_404(UserProfileInfo, user_profile=user_id)
        user = get_object_or_404(User, id=profile.id)
        profile_info_form = UserProfileInfoForm(instance=profile)
        user_info_form = UserForm(instance=user)
        return render(request, 'user_update_form.html', {'profile_info_form': profile_info_form, 'user_info_form':user_info_form})

    def post(self, request, *args, **kwargs): 
        # user_id = kwargs.get('pk')
        user_id = self.request.user
        profile = get_object_or_404(UserProfileInfo, user_profile=user_id) 
        user = get_object_or_404(User, id=profile.id)  

        profile_info_form = UserProfileInfoForm(data=request.POST, instance=profile)
        user_info_form = UserForm(data=request.POST, instance=user)
        
        if user_info_form.is_valid() and profile_info_form.is_valid():
            user = user_info_form.save()
            user.save()

            profile = profile_info_form.save(commit=False)
            profile.user_profile = user
            profile.save()
            
            return redirect('/')

        return render(request, 'user_update_form.html',{'profile_info_form': profile_info_form, 'user_info_form':user_info_form})



    
class DirectSponsorTableView(SingleTableView):
    model = UserProfileInfo
    table_class = UserInfoTable
    context_object_name = 'applications'
    template_name = 'application_lists.html'

    def get_queryset(self, *args, **kwargs):
        user_id = self.request.user.id
        user = get_object_or_404(UserProfileInfo, id=user_id)
        j=user.sponsored.filter(confirm=True)
        return j


from .tables import SingleLegUserTable
class SingleLineListTableView(SingleTableView):
    model = UserProfileInfo
    table_class = SingleLegUserTable
    context_object_name = 'applications'
    template_name = 'application_lists.html'
    def get_queryset(self, *args, **kwargs):
        user_id = self.request.user.id  
        application = get_object_or_404(UserProfileInfo, id=user_id)
        k=UserProfileInfo.objects.filter(application_date__gt = application.application_date, confirm=True)

        return k  


def level_income(request, *args, **kwargs):
    user_id = kwargs.get('pk')
    user = get_object_or_404(UserProfileInfo, id=user_id)
    j=user.sponsored.all()
    return render(request, 'level_income.html')


def transfer_balance(request, *args, **kwargs):

    if request.method == "POST":
        form_is = BalanceTransferForm(data=request.POST)
        if form_is.is_valid():
            user_id = request.user
            profile = get_object_or_404(UserProfileInfo, user_profile=user_id)
            x = form_is.cleaned_data['username']
            mr_x = get_object_or_404(User, username = x)
            z = get_object_or_404(UserProfileInfo,user_profile = mr_x)
            y = form_is.cleaned_data['amount']
            if y <= profile.account:
                profile.account = profile.account-y
                profile.save()
                z.account = z.account+y
                z.save()
               
            print(form_is.cleaned_data['username'])
            print(form_is.cleaned_data['amount'])
            

            return redirect('/')
        
    form = BalanceTransferForm()
    return render(request, 'transfer_wallet.html',{'form':form})    


def activate_account(request, *args, **kwargs):
    if request.method == "POST":
        form_is = AccoutActivationForm(data=request.POST)
        if form_is.is_valid():
            x = form_is.cleaned_data['username']
            mr_x = get_object_or_404(User, username = x)
            z = get_object_or_404(UserProfileInfo,user_profile = mr_x)
            y = form_is.cleaned_data['amount']
            # import pdb;pdb.set_trace()
            print(form_is.cleaned_data['username'])
            print(form_is.cleaned_data['amount'])

            if y == 25 and z.confirm==False:
                user_id = request.user
                profile = get_object_or_404(UserProfileInfo, user_profile=user_id) 
                if profile.account>=25:
                    profile.account = profile.account-25
                    profile.save()
                 
                    z.user_confirmation()
                


                return redirect('/')
        
    form = AccoutActivationForm()

    return render(request, 'activate_account.html',{'form':form}) 

def withdrawal_fund(request, *args, **kwargs):
    if request.method == "POST":
        form_is = WithdrawalFundForm(data=request.POST)
        if form_is.is_valid():
            
            print(form_is.cleaned_data['username'])
            print(form_is.cleaned_data['amount'])
            print(form_is.cleaned_data['bitcoin_address'])
            return redirect('/')
        
    form = WithdrawalFundForm()

    return render(request, 'withdrawal_fund.html',{'form':form}) 

def reward_income(request, *args, **kwargs):
    return render(request, 'reward_income.html') 

def withdrawal_report(request, *args, **kwargs):
    return render(request, 'withdrawal_report.html')        


# def single_line(request, *args, **kwargs):
#     application_id = kwargs.get('pk')
#     application = get_object_or_404(UserProfileInfo, id=application_id)
#     k=UserProfileInfo.objects.filter(application_date__gt = application.application_date)
#     print(k)
#     return render(request, 'user_list.html',{'users':k})


# def direct_sponsor(request, *args, **kwargs):
#     user_id = kwargs.get('pk')
#     user = get_object_or_404(UserProfileInfo, id=user_id)
#     j=user.sponsored.all()
#     return render(request, 'user_list.html',{'users':j})

# class UpdateViewDash(generic.View):
    
#     def get(self, request, *args, **kwargs):
#         # user_id = kwargs.get('pk')
#         user_id = self.request.user
#         profile = get_object_or_404(UserProfileInfo, user_profile=user_id)
#         user = get_object_or_404(User, id=profile.user.id)
#         profile_info_form = UserProfileInfoForm(instance=profile)
#         user_info_form = UserForm(instance=user)
#         return render(request, 'update.html', {'profile_info_form': profile_info_form, 'user_info_form':user_info_form})

#     def post(self, request, *args, **kwargs): 
#         # user_id = kwargs.get('pk')
#         user_id = self.request.user
#         profile = get_object_or_404(UserProfileInfo, user_profile=user_id)
#         # print(profile) 
#         user = get_object_or_404(User, id=profile.user.id)  

#         # print(user)
#         profile_info_form = UserProfileInfoForm(data=request.POST, instance=profile)
#         user_info_form = UserForm(data=request.POST, instance=user)
#         # print(user_info_form.is_valid())
#         # print(profile_info_form.is_valid())
#         # import pdb;pdb.set_trace()
        
#         if user_info_form.is_valid() and profile_info_form.is_valid():
#             user = user_info_form.save()
#             user.save()

#             profile = profile_info_form.save(commit=False)
#             profile.user = user
#             profile.save()
            
#             return redirect('/')

#         return render(request, 'update.html',{'profile_info_form': profile_info_form, 'user_info_form':user_info_form})
    # def get(self, request, *args, **kwargs):
        # donation_obj = get_object_or_404(Donation, pk=kwargs.get('pk'))
        # donator_form = InvestorDetailsForm(json.loads(donation_obj.donor_details))
        # donation_form = DonationFormDash(instance=donation_obj)
        # payment_form = PaymentForm(instance=donation_obj.payment)
        # return render(request, 'cclportal/donation_form_dash.html', {'donator_form': donator_form, 'donation_form': donation_form, 'payment_form': payment_form})

    # def post(self, request, *args, **kwargs):
        # donation_obj = get_object_or_404(Donation, pk=kwargs.get('pk'))
        # donator_form = InvestorDetailsForm(request.POST or None, request.FILES)
        # payment_form = PaymentForm(request.POST or None, instance=donation_obj.payment)
        # donation_form = DonationFormDash(request.POST or None, instance=donation_obj)

        # if donator_form.is_valid() and donation_form.is_valid():
            # donator_image = request.FILES.get('image')
            # donator_data = donator_form.cleaned_data
            # if donator_image:
                # fs = FileSystemStorage()
                # donator_image_filename = fs.save(donator_image.name, donator_image)
                # donator_image_url = fs.url(donator_image_filename)
                # donator_data['image'] = donator_image_url
            # donation_obj = donation_form.save(commit=False)
            # donation_obj.donor_details = json.dumps(donator_data)
            # if payment_form.is_valid():
                # payment_obj = payment_form.save()
                # donation_obj.payment = payment_obj
            # donation_obj.save()
            # return redirect('/')

        # return render(request, 'cclportal/donation_form_dash.html',{'donator_form': donator_form, 'donation_form': donation_form, 'payment_form': payment_form})



#     # import pdb;pdb.set_trace()
    # if request.user == True :
     


    # return redirect('accounts/login/')


# # def registration(request):
# #     forms = RegistrationFromA
# #     return render(request,'form.html',{'forms':forms})

# class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
#     model = User
#     fields = ['username', 'first_name', 'last_name']
#     context_object_name = 'user_detail'
#     template_name = 'profile_details.html'

# class RegistrationView(LoginRequiredMixin,CreateView):
#     model = Application   
#     fields = '__all__'
#     template_name = 'form.html'
#     context_object_name = 'applications'
#     success_url = reverse_lazy('member:home')

# class ApplicationListView(ListView):
#     model = Application
#     context_object_name = 'applications'
#     template_name = 'application_list.html'

# class UserListTableView(SingleTableView):
#      model = UserProfileInfo
#      table_class = UserInfoTable
#      context_object_name = 'applications'
#      template_name = 'application_lists.html'


# class ApplicationDetailsView(DetailView):
#     model = Application   
#     context_object_name = 'application'
#     template_name = 'application_details.html'   


# class ApplicationDeleteView(DeleteView):
#     model = Application
#     success_url = reverse_lazy('member:applicationtable')      

# def approve_user(request, *args , **kwargs):
    
#     application_id = kwargs.get('pk')

#     application = get_object_or_404(Application, id=application_id)
#     from django.contrib.auth.hashers import make_password
#     hashed_password = make_password(application.password)
#     member = User.objects.create(
#             username = application.username,
#             first_name = application.first_name,
#             last_name = application.last_name,
#             password = hashed_password,
#             is_active = True,
#             is_staff = True
#             )
#     member.save()        
#     return redirect('member:home')



# def member_list(request, *args, **kwargs):
    #     application_id = kwargs.get('pk')
#     application = get_object_or_404(UserProfileInfo, id=application_id)
#     k=User.objects.all()
#     j=application.sponsored.all()
#     print(j)
#     return render(request, 'user_list.html',{'users':j})



# def downline_team_member(request, *args, **kwargs):
    #     user_id = kwargs.get('pk')
#     user = get_object_or_404(UserProfileInfo, id=user_id)
#     # member = StaffMember.objects.get(id__id=user_id)

#     new_list = [user]

    

#     def get_final_team(qs):
#         team = []
#         staffmembers = UserProfileInfo.objects.filter(sponsor__in=qs)

#         team += staffmembers 
#         if staffmembers:
#             interim_team_qs = get_final_team(staffmembers)
#             for qs in interim_team_qs:
#                 team.append(qs)
#         else:
#             team = [qs]

#         return team
#     new_list = get_final_team(new_list)

#     number = len(new_list)
#     # to find the index of user
#     # number = new_list.index(user)
    
#     return render(request, 'user_list.html',{'users':new_list,'number':number})    

# class DownlineTeamTableView(SingleTableView):
#     model = UserProfileInfo
#     table_class = UserInfoTable
#     context_object_name = 'applications'
#     template_name = 'application_lists.html'

#     def get_queryset(self, *args, **kwargs):
#         user_id = self.request.user.id
#         # user_id = kwargs.get('pk')
#         # print(user_id)
#         # import pdb;pdb.set_trace()

#         user = get_object_or_404(UserProfileInfo, id=user_id)
#         # member = StaffMember.objects.get(id__id=user_id)
        
#         new_list = [user]

#         def get_final_team(qs):
#             team = []
#             staffmembers = UserProfileInfo.objects.filter(sponsor__in=qs)

#             team += staffmembers 
#             if staffmembers:
#                 interim_team_qs = get_final_team(staffmembers)
#                 for qs in interim_team_qs:
#                     team.append(qs)
#             # else:
#                 # team = [qs]

#             return team
#         # import pdb;pdb.set_trace()    
#         new_list = get_final_team(new_list)
        

#         return new_list    

# def activity(self):

#     user_is = get_object_or_404(UserProfileInfo, user_profile=self.user)
#     downline_number = list(UserProfileInfo.objects.filter(application_date__gt = user_is.application_date, confirm=True).order_by('confirmation_date'))
#     direct_users =list(UserProfileInfo.objects.filter(confirm = True, sponsor = user_is ).order_by('confirmation_date'))
#     if (len(downline_number)>=20 and len(downline_number)<40) and len(direct_users)==1:
#         obj = Activity.objects.create()
#         obj.level = 1
#         obj.user = user_is
#         x = downline_number[19]
#         date_of_user_20 = x.confirmation_date
#         y = direct_users[0]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_20>date_of_first_user:

#             obj.start_date = date_of_user_20                    
#         else:
#             obj.start_date = date_of_first_user

#         obj.end_date = obj.start_date + timedelta(days=7)    
            

#     elif (len(downline_number)>=40 and len(downline_number)<100) and len(direct_users)==2:
#         pre_obj=Activity.objects.filter(level=1, user=user_is)
#         pre_obj_end_date = pre_obj.end_date
#         obj = Activity.objects.create()
#         obj.level = 2
#         obj.user = user_is
#         x = downline_number[39]
#         date_of_user_40 = x.confirmation_date
#         y = direct_users[1]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_40>date_of_first_user and date_of_user_40>pre_obj_end_date :
#             obj.start_date = date_of_user_40
#         elif date_of_first_user>date_of_user_40 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days=7) 
   

#     elif (len(downline_number)>=100 and len(downline_number)<200) and len(direct_users)==3:
#         pre_obj=Activity.objects.filter(level=2, user=user_is)
#         pre_obj_end_date = pre_obj.end_date
        
#         obj = Activity.objects.create()
#         obj.level = 3
#         obj.user = user_is
#         x = downline_number[99]
#         date_of_user_100 = x.confirmation_date
#         y = direct_users[2]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_100>date_of_first_user and date_of_user_100>pre_obj_end_date :
#             obj.start_date = date_of_user_100
#         elif date_of_first_user>date_of_user_100 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1) 

#         obj.end_date = obj.start_date + timedelta(days=7) 

#     elif (len(downline_number)>=200 and len(downline_number)<400) and len(direct_users)==4:
#         pre_obj=Activity.objects.filter(level=3, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 4
#         obj.user = user_is
#         x = downline_number[199]
#         date_of_user_200 = x.confirmation_date
#         y = direct_users[3]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_200>date_of_first_user and date_of_user_200>pre_obj_end_date :
#             obj.start_date = date_of_user_200
#         elif date_of_first_user>date_of_user_200 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days=7) 

#     elif (len(downline_number)>=400 and len(downline_number)<1000) and len(direct_users)==5:
#         pre_obj=Activity.objects.filter(level=4, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 5
#         obj.user = user_is
#         x = downline_number[399]
#         date_of_user_400 = x.confirmation_date
#         y = direct_users[4]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_400>date_of_first_user and date_of_user_400>pre_obj_end_date :
#             obj.start_date = date_of_user_400
#         elif date_of_first_user>date_of_user_400 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7) 

#     elif (len(downline_number)>=1000 and len(downline_number)<2000) and len(direct_users)==6:
#         pre_obj=Activity.objects.filter(level=5, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 6
#         obj.user = user_is

#         x = downline_number[999]
#         date_of_user_1000 = x.confirmation_date
#         y = direct_users[5]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_1000>date_of_first_user and date_of_user_1000>pre_obj_end_date :
#             obj.start_date = date_of_user_1000
#         elif date_of_first_user>date_of_user_1000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date

#         obj.end_date = obj.start_date + timedelta(days = 7) 

#     elif (len(downline_number)>=2000 and len(downline_number)<3000) and len(direct_users)==7:
#         pre_obj=Activity.objects.filter(level=6, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 7
#         obj.user = user_is
#         x = downline_number[1999]
#         date_of_user_2000 = x.confirmation_date
#         y = direct_users[6]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_2000>date_of_first_user and date_of_user_2000>pre_obj_end_date :
#             obj.start_date = date_of_user_2000
#         elif date_of_first_user>date_of_user_2000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)

#     elif (len(downline_number)>=3000 and len(downline_number)<4000) and len(direct_users)==8:
#         pre_obj=Activity.objects.filter(level=7, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 8
#         obj.user = user_is
#         x = downline_number[2999]
#         date_of_user_3000 = x.confirmation_date
#         y = direct_users[7]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_3000>date_of_first_user and date_of_user_3000>pre_obj_end_date :
#             obj.start_date = date_of_user_3000
#         elif date_of_first_user>date_of_user_3000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)
        
#         obj.end_date = obj.start_date + timedelta(days = 7)


#     elif (len(downline_number)>=4000 and len(downline_number)<5000) and len(direct_users)==9:
#         pre_obj=Activity.objects.filter(level=8, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 9
#         obj.user = user_is
#         x = downline_number[3999]
#         date_of_user_4000 = x.confirmation_date
#         y = direct_users[8]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_4000>date_of_first_user and date_of_user_4000>pre_obj_end_date :
#             obj.start_date = date_of_user_4000
#         elif date_of_first_user>date_of_user_4000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)
        
#         obj.end_date = obj.start_date + timedelta(days = 7)

#     elif (len(downline_number)>=5000 and len(downline_number)<7500) and len(direct_users)==10:
#         pre_obj=Activity.objects.filter(level=9, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 10
#         obj.user = user_is
#         x = downline_number[4999]
#         date_of_user_5000 = x.confirmation_date
#         y = direct_users[9]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_5000>date_of_first_user and date_of_user_5000>pre_obj_end_date :
#             obj.start_date = date_of_user_5000
#         elif date_of_first_user>date_of_user_5000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)
        
#         obj.end_date = obj.start_date + timedelta(days = 7)

#     elif (len(downline_number)>=7500 and len(downline_number)<9000) and len(direct_users)==11:
#         pre_obj=Activity.objects.filter(level=10, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 11
#         obj.user = user_is
#         x = downline_number[7499]
#         date_of_user_7500 = x.confirmation_date
#         y = direct_users[10]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_7500>date_of_first_user and date_of_user_7500>pre_obj_end_date :
#             obj.start_date = date_of_user_7500
#         elif date_of_first_user>date_of_user_7500 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)

#     elif (len(downline_number)>=9000 and len(downline_number)<12000) and len(direct_users)==12:
#         pre_obj=Activity.objects.filter(level=11, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 12
#         obj.user = user_is
#         x = downline_number[8999]
#         date_of_user_9000 = x.confirmation_date
#         y = direct_users[11]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_9000>date_of_first_user and date_of_user_9000>pre_obj_end_date :
#             obj.start_date = date_of_user_9000
#         elif date_of_first_user>date_of_user_9000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)

#     elif (len(downline_number)>=12000 and len(downline_number)<13000) and len(direct_users)==13:
#         pre_obj=Activity.objects.filter(level=12, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 13
#         obj.user = user_is
#         x = downline_number[11999]
#         date_of_user_12000 = x.confirmation_date
#         y = direct_users[12]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_12000>date_of_first_user and date_of_user_12000>pre_obj_end_date :
#             obj.start_date = date_of_user_12000
#         elif date_of_first_user>date_of_user_12000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)    

#     elif (len(downline_number)>=13000 and len(downline_number)<18000) and len(direct_users)==14:
#         pre_obj=Activity.objects.filter(level=13, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 14
#         obj.user = user_is
#         x = downline_number[12999]
#         date_of_user_13000 = x.confirmation_date
#         y = direct_users[13]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_13000>date_of_first_user and date_of_user_13000>pre_obj_end_date :
#             obj.start_date = date_of_user_13000
#         elif date_of_first_user>date_of_user_13000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)


#     else (len(downline_number)>=18000) and len(direct_users)==15:
#         pre_obj=Activity.objects.filter(level=14, user=user_is)
#         pre_obj_end_date = pre_obj.end_date

#         obj = Activity.objects.create()
#         obj.level = 15
#         obj.user = user_is
#         x = downline_number[17999]
#         date_of_user_18000 = x.confirmation_date
#         y = direct_users[14]
#         date_of_first_user = y.confirmation_date
#         if date_of_user_18000>date_of_first_user and date_of_user_18000>pre_obj_end_date :
#             obj.start_date = date_of_user_18000
#         elif date_of_first_user>date_of_user_18000 and date_of_first_user>pre_obj_end_date:
#             obj.start_date = date_of_first_user
#         else
#             obj.start_date = pre_obj_end_date + timedelta(days=1)

#         obj.end_date = obj.start_date + timedelta(days = 7)    

    
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import hashlib
from . import md5hash


def cryptobox_rendering(request):
    boxID = 1234    # Your gourl cryptobox ID, https://gourl.io/editrecord/coin_boxes/0
    coin_name = 'bitcoin'
    public_key = 'your-gourl_public-key'
    private_key = 'your-gourl_private-key'
    webdev_key  = 'optional your-web-developer-key'
    amount = 0  # amount in bitcoins (Or another crybtocurrency
    period = '1 MINUTE'
    amountUSD = 5
    userID = request.user.username
    language = 'en'
    iframeID = 'iframeID'
    orderID = 'product-1'
    width = 530
    height = 230
    md5 = md5hash.hash(boxID, coin_name, public_key, private_key, webdev_key, amount,
                        period, amountUSD, userID, language, iframeID, orderID,
                        width, height)
    variables = {'boxID': boxID, 'coin_name': coin_name, 'public_key': public_key, 'webdev_key': webdev_key,
                 'amount': amount, 'period': period, 'amountUSD': amountUSD, 'userID': userID, 'language': language,
                 'iframeID': iframeID, 'orderID': orderID, 'width': width, 'height': height, 'hash': md5}
    return render(request, 'cryptobox_template.html', variables)

    
@csrf_exempt     # Very important! You need to allow a Foreign site (Gourl server) communicate with your server
def callback(request, *args, **kwargs):
    html = ""
    if request.method == 'POST':
        private_key = "Your-cryptobox-private-key"
        h = hashlib.sha512(private_key.encode(encoding='utf-8'))    # The incoming 'private_key' data from Gourl is sha512 encrypted
        private_key_hash = h.hexdigest()    # Hence, you need to hash your private key too for make security check
        if (request.POST.get('confirmed') == '0' and request.POST.get('box') == 'box-number' and
                request.POST.get('status') == 'payment_received' and
                request.POST.get('private_key_hash') == private_key_hash):     # Make the checks you need (Don't forget to check the 'private_key_hash')
            """
               Your code here for getting a unconfirmed payment    
            """
            html = "cryptobox_newrecord"     # Don't change this text. It's used by gourl server
        elif request.POST.get('confirmed') == '1':
        
        #    Your code here for a payment confirmation
        
            html = "cryptobox_updated"        # Don't change it
        else:
        
        #    Your code here
        
            html = "cryptobox_nochanges"    # Don't change it

    else:
        html = "Only POST Data Allowed"     # Don't change it

    return HttpResponse(html)


   