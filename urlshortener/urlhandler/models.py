from django.db import models

# Create your models here.

class shorturl(models.Model):
    original_url = models.URLField(blank=False)
    short_url = models.CharField(blank=False, max_length=10)
    visits = models.IntegerField(default=0)
