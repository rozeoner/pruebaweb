from django.db import models

# Create your models here.
class Company(models.Model):
        name = models.CharField(max_length=100)

class Envelope(models.Model):
    amount = models.IntegerField()
    motivation = models.CharField(max_length=100)
    company = models.ForeingKey(Company, on_delete=models.CASCADE)
