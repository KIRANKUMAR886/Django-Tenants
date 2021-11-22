from django.contrib import admin
from attendance_shared.models import *

@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display=('store_id','branch_id','address','store_mobile','store_unique_id','org_id')
