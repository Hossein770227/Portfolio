from django.contrib import admin

from .models import RecevieMessage , Skills, Portfolio

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display= ['name','course','date_time_create','active']
    ordering = ['date_time_create']




@admin.register(RecevieMessage)
class ReciveMessageAdmin(admin.ModelAdmin):
    list_display= ['full_name','email','date_time_create',]
    ordering = ['date_time_create']


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ['name', 'date_time_created']
