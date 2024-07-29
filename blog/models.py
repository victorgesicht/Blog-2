from django.db import models

# Create your models here.

class article(models.Model):
    author=models.CharField(max_length=40, blank=False, null=True)
    title=models.CharField(max_length=40, blank=False, null=True)
    