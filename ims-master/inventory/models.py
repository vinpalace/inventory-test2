from django.db import models
from decimal import Decimal


class Product(models.Model):
    ip_address = models.CharField(max_length=200, blank=True, null=True, default='0.0.0.0')
    info = models.CharField(max_length=200, blank=True, null=True, default=' ')
    hostname = models.CharField(max_length=200, blank=True, null=True, default=' ')
    able_to_ping = models.CharField(max_length=200, blank=True,null=True, default=' ')
    able_to_login = models.CharField(max_length=200,blank=True, null=True, default=' ')
    physical_or_vm = models.CharField(max_length=200, blank=True,null=True, default=' ')
    issues = models.CharField(max_length=200, blank=True,null=True, default='None')

    # def __str__(self):
    #     return 'Id:{0} Name:{1}'.format(self.id, self.name)
