from django.db import models

# Create your models here.
class Checkout(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    success_url = models.URLField()
    cancel_url = models.URLField()