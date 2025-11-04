from django.db import models

# Create your models here.

class Change(models.Model):
    chg_number = models.CharField(max_length=10)
    chg_title = models.CharField(max_length=80,unique=True)
    chg_text = models.TextField(default="")

    def __str__(self):
        return f'{self.chg_number} - {self.chg_title}'

class VServer(models.Model):
    vs_shortname = models.CharField(max_length=10,unique=True)
    vs_type = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.vs_shortname}'

