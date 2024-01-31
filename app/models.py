from django.db import models

# Create your models here.




class Records(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    attendance = models.BooleanField(default=False)
    class Meta:
        db_table="records"

