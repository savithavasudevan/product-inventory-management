from django.db import models

# Create your models here.
class Productmodel(models.Model):

    name=models.CharField(max_length=100)

    category=models.CharField(max_length=100)

    price=models.DecimalField(max_digits=5,decimal_places=2)

    quantity=models.IntegerField()

    date_added=models.DateTimeField()