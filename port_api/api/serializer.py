from rest_framework import serializers
from .models import Home

class homeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    image_url = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Home.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.title = validated_data.get('title', instance.title)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance
