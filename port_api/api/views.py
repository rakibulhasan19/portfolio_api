from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import homeModel
from .serializer import homeSerializer

# Create your views here.
@csrf_exempt
def home_list_get(request):
    if request.method == 'GET':
        data = homeModel.objects.all()
        serialier = homeSerializer(data,many=True)
        return JsonResponse(serialier.data,safe=False)

    if request.method =='POST':
        data = JSONParser().parse(request)
        serializer = homeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def home_details(request,pk):
    try:
        details = homeModel.objects.get(pk=pk)
    except homeModel.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = homeSerializer(details)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = homeSerializer(details,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=205)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        details.delete()
        return HttpResponse(status=204)
