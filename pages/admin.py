from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import RecevieMessage , Skills, OtherSkills

@admin.register(Skills)
class SkillAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display= ['name','course','date_time_create','active']
    ordering = ['date_time_create']


@admin.register(OtherSkills)
class OtherSkillsAdmin(admin.ModelAdmin):
    list_display= ['name','course','date_time_create','active']
    ordering = ['date_time_create']





@admin.register(RecevieMessage)
class ReciveMessageAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display= ['full_name','email','date_time_create',]
    ordering = ['date_time_create']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')
