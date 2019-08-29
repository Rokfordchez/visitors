from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UList(models.Model):
    user = models.ForeignKey(User, blank=True,
        null=True, on_delete=models.CASCADE)
    visitor = models.TextField(default='anonymous')
    visit_num = models.PositiveIntegerField(default=0)
    data = models.TextField(blank=True)


