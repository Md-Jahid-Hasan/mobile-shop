from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

GENDER = [
    ('Woman', 'Woman'),
    ('Man', 'Man'),
    ('Other', 'Other'),
]


class Address(models.Model):
    district = models.CharField(max_length=10)
    sub_district = models.CharField(max_length=15)
    road_number = models.CharField(max_length=10)
    area = models.CharField(max_length=30)
    content_type = models.OneToOneField(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = 'Addresses'


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_details')
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER, default='Woman', max_length=6)
    address = GenericRelation(Address, related_query_name='person')


class Machine(models.Model):
    machine_code = models.CharField(max_length=15)
    product_quantity = models.PositiveIntegerField()
    is_available = models.BooleanField()
    is_empty = models.BooleanField()
    address = GenericRelation(Address, related_query_name='machine')

