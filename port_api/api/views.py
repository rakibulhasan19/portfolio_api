from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import homeModel
from .serializer import homeSerializer

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








#
# @api_view(['GET','POST'])
# def home_list_get(request):
#     if request.method == 'GET':
#         data = homeModel.objects.all()
#         serialier = homeSerializer(data,many=True)
#         return Response(serialier.data)
#
#     elif request.method =='POST':
#         serializer = homeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def home_details(request,pk):
#     try:
#         details = homeModel.objects.get(pk=pk)
#     except homeModel.DoesNotExist:
#         return HttpResponse(status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = homeSerializer(details)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = homeSerializer(details,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         details.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
