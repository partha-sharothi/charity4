# from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import get_object_or_404

from datetime import datetime
from datetime import timedelta 

# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class UserA(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
#     application_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     sponsor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

 

# class UserB(User):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     application_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
#     sponsor = models.ForeignKey('UserA', on_delete=models.CASCADE)
# class Application(models.Model):
#     username = models.CharField(max_length=120,null=True,blank=True)
#     first_name = models.CharField(max_length=120,null=True,blank=True)
#     last_name = models.CharField(max_length=120,null=True,blank=True)
#     password = models.CharField(max_length = 123, null=True, blank=True)
#     phone_number = PhoneNumberField(null=True,blank=True)
#     email = models.EmailField(max_length=120,blank=True,null=True)
#     sponsor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name = 'members')
#     application_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


#     def __str__(self):
#         return str(self.username)

    # def __str__(self):
    #         return "<members: {} {}>".format(self.first_name, self.last_name)

    # def __repr__(self):
    #     return self.__str__()    
    

from django.db import models
from django.contrib.auth.models import User
import pytz

utc=pytz.UTC





# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete='CASCADE',name='user_profile')
    phone_number = PhoneNumberField(null=True,blank=True)
    confirm = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField( null=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sponsor = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE, null=True, blank=True,related_name ='sponsored' )
    country = models.ForeignKey('Country',on_delete='CASCADE', null=True , blank = True)
    active = models.BooleanField(default=False)
    # wallet = models.OneToOneField('EWallet',on_delete='CASCADE',null=True, blank=True)
    account = models.IntegerField(default=0)


    
    def __str__(self):
        return self.user_profile.username

    def user_confirmation(self):
        self.confirm = True
        self.confirmation_date = utc.localize(datetime.now())
        self.active = True
        self.save()
        return None

    def level_bonus(self):
        user = self.user
        user = get_object_or_404(UserProfileInfo, user_profile=user)
        # k=UserProfileInfo.objects.all()
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

        refferal_bonus=((float(len(name1))*(50.0*10/100))+(float(len(name2))*(50.0*5/100))+(float(len(name3))*(50.0*3/100))+
            (float(len(name4))*(50.0*2/100))+(float(len(name5))*(50*1/100))+
            (float(len(name6))*(50.0*1/200))+(float(len(name7))*(50.0*1/200))+(float(len(name8))*(50.0*1/200))+
            (float(len(name9))*(50.0*1/200))+(float(len(name10))*(50.0*1/200)))

        return refferal_bonus         




class Country(models.Model):
    country = models.CharField(max_length=150)
    flag = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.country


class Activity(models.Model):
    level = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,null=True, blank=True)
    level_status = models.BooleanField(default=False)

    def level_status_check(self):
        
        if (self.end_date) <= utc.localize(datetime.now()):
            self.level_status = True
            self.save()

            
        return None    




# class EWallet(models.Model):
#     ammount = models.IntegerField(default=0)
