from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
