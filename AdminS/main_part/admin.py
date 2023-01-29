from django.contrib import admin

from .models import *


class MainDataAdmin(admin.ModelAdmin):
    list_display = ('id','year', 'cemetery_name', 'number', 'surname', 'name', 'middle_name', 'age_deceased', 'date_of_birth', 'date_of_death', 'burial_date', 'area', 'grave', 'evidence', 'registry_office', 'responsible_for_burial', 'note', 'user_create','data_create', 'del_status', 'del_user', 'del_data')

admin.site.register(User)
admin.site.register(MainData, MainDataAdmin)