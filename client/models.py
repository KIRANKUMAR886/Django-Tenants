from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    Org_uuid = models.CharField(max_length=255, unique=True)
    Org_Name = models.CharField(max_length=255) 
    Subscription_id = models.IntegerField()
    Email_id = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    City= models.CharField(max_length=255)
    Status= models.BooleanField()
    State= models.CharField(max_length=255)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass