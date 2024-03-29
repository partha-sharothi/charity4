from django.forms import ModelForm
from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User
# from member.models import UserA

# class RegistrationFromA(ModelForm):
#     class Meta:
#         model  = UserA
#         fields = ['first_name','last_name']

class UserProfileInfoForm(ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('phone_number','sponsor','country')

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')        


class BalanceTransferForm(forms.Form):
    username = forms.CharField(max_length = 150)
    amount = forms.IntegerField()

class AccoutActivationForm(forms.Form):
    username = forms.CharField(max_length = 150)
    amount = forms.IntegerField()

class WithdrawalFundForm(forms.Form):
    username = forms.CharField(max_length = 150)
    amount = forms.IntegerField() 
    bitcoin_address = forms.CharField(max_length = 200)


class BitcoinDetailForm(forms.Form):
    bitcoin_address = forms.CharField(max_length = 200)
    otp = forms.CharField(max_length = 150)