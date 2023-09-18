from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=250)
    page_count = models.IntegerField()
    stock = models.BooleanField()
    price = models.FloatField()
    image = models.ImageField(blank=True,null=True)
    
    