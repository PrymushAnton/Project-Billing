from django.db import models

# Create your models here.
class Contract(models.Model):
    building = models.CharField(null=True, blank=True,max_length=255, default=None)
    number_of_contract = models.CharField(null=True, blank=True,max_length=255, default=None)
    date_beginning = models.DateField(null=True, blank=True,default=None)
    date_end = models.DateField(null=True, blank=True,default=None)
    date_of_agreement = models.DateField(null=True, blank=True,default=None)
    landlord = models.CharField(null=True, blank=True,max_length=255, default=None)
    tenant = models.CharField(null=True, blank=True,max_length=255, default=None)
    tenant_ps = models.CharField(null=True, blank=True,max_length=255, default=None)
    type_of_contract = models.CharField(null=True, blank=True,max_length=255, default=None)
    tax_for_ad = models.CharField(null=True, blank=True,max_length=255, default=None)
    in_work = models.CharField(null=True, blank=True,max_length=255, default=None)
    closed = models.CharField(null=True, blank=True,max_length=255, default=None)
    comment = models.CharField(null=True, blank=True,max_length=255, default=None)
    number_of_agreement = models.CharField(null=True, blank=True,max_length=255, default=None)
    main_agreement = models.CharField(null=True, blank=True,max_length=255, default=None)
    lot = models.CharField(null=True, blank=True,max_length=255, default=None)