from django.db import models
from django.core import validators
from django import forms
import re
from django.core.exceptions import ValidationError
# Create your models here.

from django.contrib.auth.models import AbstractUser
def num_plate(value):
    pattern = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
    result = re.match(pattern, value)
    if not result:
        raise ValidationError('Enter valid Numberplate')
    return



class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Area(models.Model):
    area_city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name

class OWNUSER(AbstractUser):
    company_name = models.CharField(blank=True,max_length=100)
    UPI_no = models.IntegerField(null=True)
    mobile_no = models.CharField(blank = False, max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    address = models.CharField(blank=True, max_length=500)



class provide(models.Model):
    p_pickup_city = models.ForeignKey(City,related_name="pro_pi",on_delete=models.CASCADE)
    p_dest_city = models.ForeignKey(City,related_name="pro_de",on_delete=models.CASCADE)
    remaining_weight = models.IntegerField(null = False)
    rate = models.IntegerField(null = False)
    total_capacity = models.IntegerField(null = False)
    numberplate_no = models.CharField(validators = [num_plate],max_length=10)
    permits = models.CharField(null = True,max_length=20)
    typeof_vehicle = models.CharField(null = False,max_length=20)
    typeof_payment = models.CharField(null = True,max_length=20)
    who_provider = models.ForeignKey(OWNUSER,null=True,blank=True,on_delete=models.CASCADE,related_name="who_is_provider")
    who_seeker = models.ForeignKey(OWNUSER,null=True,blank=True, on_delete=models.CASCADE,related_name="who_is_seeker")
    accepted = models.BooleanField(default=False)


class seek(models.Model):
    s_pickup_city = models.ForeignKey(City,related_name="Seek_pi",on_delete=models.CASCADE)
    s_dest_city = models.ForeignKey(City,related_name="Seek_de",on_delete=models.CASCADE)
    total_weight = models.IntegerField(null = False)
    rate = models.IntegerField(null = True)
    typeof_vehicle = models.CharField(null = True,max_length=20)
    nameof_goods = models.CharField(null = False,max_length=20)
    status = models.IntegerField(default = 0)
    who_seeker = models.ForeignKey(OWNUSER,on_delete=models.CASCADE,related_name="who_is_seeker_in_seeker")
    who_provider = models.ForeignKey(OWNUSER,null=True,on_delete=models.CASCADE,related_name="who_is_provider_in_seeker")


class deal(models.Model):
    provider_id = models.OneToOneField(provide,on_delete=models.CASCADE)
    seeker_id = models.OneToOneField(seek,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False,auto_now=True)
