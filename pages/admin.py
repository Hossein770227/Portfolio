from django.contrib import admin

from .models import RecevieMessage , Skills

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display= ['name','course','date_time_create','active']
    ordering = ['date_time_create']




@admin.register(RecevieMessage)
class ReciveMessageAdmin(admin.ModelAdmin):
    list_display= ['full_name','email','date_time_create',]
    ordering = ['date_time_create']

