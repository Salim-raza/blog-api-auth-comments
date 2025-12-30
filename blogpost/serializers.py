from rest_framework import serializers
from .models import *


class PostCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ["author"]
        

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class PostUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "description", "image", "category"]
        
    def update(self, instance, validated_data):
        if "image" in validated_data:
            if instance.image:
                instance.image.delete(save=False)
        return super().update(instance, validated_data)
    
class CommentSerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.email", read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "post", "user", "user_name", "content", "created_at", "updated_at"]
        read_only_fields = ["user", "post"]
        
class CommentUpdateSerializers(serializers.Serializer):
    content = serializers.CharField()
    
    def update(self, instance, validated_data):
        instance.content =validated_data.get("content", instance.content)
        instance.save()
        return instance