from django.db import models


class Cars(models.Model):
    CarsId = models.AutoField(primary_key=True)
    cars_model = models.CharField(max_length=500)
    cars_price = models.CharField(max_length=500)
    cars_TKZ = models.CharField(max_length=500)
    cars_credit = models.CharField(max_length=500)
    cars_price_credit_in_month = models.CharField(max_length=500)
    cars_meliage = models.CharField(max_length=500)
    cars_date_city = models.CharField(max_length=500)

