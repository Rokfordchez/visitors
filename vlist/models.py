from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UList(models.Model):
    user = models.ForeignKey(User, blank=True,
                             null=True, on_delete=models.CASCADE)
    visitor = models.TextField(default='anonymous')
    data = models.TextField(blank=True)
    image = models.ImageField(blank=True)
