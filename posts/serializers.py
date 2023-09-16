from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostModel



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username', 'password']



# Serializer for Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        # fields = ['id', 'title', 'content', 'created_at']
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user