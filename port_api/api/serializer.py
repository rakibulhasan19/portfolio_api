from rest_framework import serializers
from .models import homeModel,aboutModel

class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model=homeModel
        fields = ['id','name','title','image_url']

class aboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=aboutModel
        fields= ['id','title','about_me','name','dob','institute','degree','city','cv','img_url']
