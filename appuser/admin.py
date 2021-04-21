from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(OWNUSER)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','state_name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','city_name','city_state']

@admin.register(provide)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','p_pickup_city','p_dest_city']

@admin.register(seek)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','s_pickup_city','s_dest_city']

@admin.register(deal)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','provider_id','seeker_id']
