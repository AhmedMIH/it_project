from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100,default='')
    descr = models.CharField(max_length=300)
    total_ticket = models.IntegerField(default=50)
    available_ticket = models.IntegerField(default=50)
    imageurl = models.URLField(max_length=300)
    country = models.CharField(max_length=20)
    year = models.IntegerField(default=2010)
    category = models.CharField(max_length=50)





