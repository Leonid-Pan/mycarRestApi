from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Cars
from .serializers import CarSerializer
# Create your views here.

@csrf_exempt
def carApi(request):
    if request.method == "GET":
        cars = Cars.objects.all()
        cars_serializer = CarSerializer(cars, many=True)
        return JsonResponse(cars_serializer.data, safe=False)

