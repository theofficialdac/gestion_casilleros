
from django.db import models
from django.contrib.auth.models import User

class Furniture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

class Locker(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='available')
