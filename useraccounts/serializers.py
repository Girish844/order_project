from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=["restro1","restro2","restro3","restro4"]

# class ArticleSerializer(serializers.Serializer):
#     restro1 = serializers.CharField(max_length=100)
#     restro2 = serializers.CharField(max_length=100)
#     restro3 = serializers.CharField(max_length=100)
#     restro4 = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.restro1 = validated_data.get('restro1', instance.restro1)
#         instance.restro2 = validated_data.get('restro2', instance.restro2)
#         instance.restro3 = validated_data.get('restro3', instance.restro3)
#         instance.restro1 = validated_data.get('restro4', instance.restro4)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance