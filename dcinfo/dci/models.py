from django.db import models

# Create your models here.

class Change(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=80)


