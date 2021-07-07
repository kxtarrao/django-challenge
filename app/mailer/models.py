#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)
    order_sum = models.DecimalField(max_digits=18, decimal_places=9, default=float(0))
    order_count = models.IntegerField(default=float(0))

    def get_order_count(self):
        return self.order_count

    def get_order_sum(self):
        return self.order_sum


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    order_count = models.IntegerField(default=float(0))

    def get_order_count(self):
        return self.order_count


@python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(Company, related_name="orders")
    contact = models.ForeignKey(Contact, related_name="orders")
    total = models.DecimalField(max_digits=18, decimal_places=9)
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.order_number
