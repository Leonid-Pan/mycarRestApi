from rest_framework import serializers
from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('CarsId', 'cars_model', 'cars_price', 'cars_TKZ', 'cars_credit', 'cars_price_credit_in_month', 'cars_meliage', 'cars_date_city')