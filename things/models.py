from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validateQuantity(value):
    if value <0 or value < 100:
        raise ValidationError
class Thing(models.Model):
    name = models.CharField(primary_key=True, max_length=30, null=False)
    description = models.TextField(max_length=120, null=True, unique=True)
    quantity = models.IntegerField(validators=validateQuantity)