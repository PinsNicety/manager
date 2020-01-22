from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Entry(models.Model):
    """ This model is for all time entries. """

    site = models.CharField(max_length=50)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    comments = models.TextField(max_length=200)
    total_time = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.site


class Expense(models.Model):
    """ This model is for all expenses. """

    site = models.CharField(max_length=50)
    miles = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.site
