from django.contrib import admin

from .models import RecevieMessage


@admin.register(RecevieMessage)
class ReciveMessageAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','email','date_time_create',]
    ordering = ['date_time_create']

