from rest_framework import serializers
from .models import homeModel


class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model=homeModel
        fields = ['id','name','title','image_url']
