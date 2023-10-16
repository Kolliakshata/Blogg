# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, BlockedUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created_at', 'updated_at')

class BlockedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedUser
        fields = ('id', 'user', 'blocked_user')
