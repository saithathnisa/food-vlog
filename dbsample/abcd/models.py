from django.db import models
class sample(models.Model):
    name=models.CharField(max_length=250)
    xyz=models.TextField()


# Create your models here.
class smp2(models.Model):
    x=models.CharField(max_length=10)

