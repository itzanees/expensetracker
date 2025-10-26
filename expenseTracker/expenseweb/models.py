from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expenses(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.category