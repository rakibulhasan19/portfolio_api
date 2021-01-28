from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import homeModel

from .serializer import homeSerializer

# Create your views here.
def home_list_get(request):
    if request.method == 'GET':
        data = homeModel.objects.all()
        serialier = homeSerializer(data,many=True)
        return JsonResponse(serialier.data,safe=False)

    if request.method =='POST':
        try:
            data = JSONParser().parse(request)
            serializer = homeSerializer(data=data)
            if serialier.is_valid:
                serialier.save()
                return JsonResponse(serializer.data, status=201)
        except:
            return JsonResponse(serializer.errors, status=400)
