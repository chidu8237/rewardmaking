from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class task(models.Model):
    link=models.URLField(max_length=200)
    pass
