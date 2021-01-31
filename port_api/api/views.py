from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import homeModel,aboutModel
from .serializer import homeSerializer,aboutSerializer

# Create your views here.
class homeList(APIView):
    def get(self,request):
        data = homeModel.objects.all()
        serializer = homeSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request):
        serializer = homeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class homeDetails(APIView):
    def get_object(self,id):
        try:
            return homeModel.objects.get(id=id)
        except homeModel.DoesNotExits:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        data = self.get_object(id)
        serializer = homeSerializer(data)
        return Response(serializer.data,status.HTTP_200_OK)

    def put(self,request,id):
        data = self.get_object(id)
        serializer = homeSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        data = self.get_object(id)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class aboutList (APIView):
    def get(self,request):
        data = aboutModel.objects.all();
        serializer = aboutSerializer(data,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    def post(self,request):
        print(request.data)
        serializer = aboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
class aboutDetails(APIView):
    def get_object(self,request,id):
        try:
            return aboutModel.objects.get(id=id)
        except aboutModel.DoesNotExits:
            return Response(status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        data = self.get_object(id)
        serializer = aboutSerializer(data=data)
        return Response(serializer.data)
    def put(self,request,id):
        data = self.get_object(id)
        serializer = aboutSerializer(data,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        data = self.get_object(id)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)

