from django.contrib import admin

# Register your models here.

from attendance_tenant.models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=('store_id','branch_id','address','store_mobile','store_unique_id','org_id')