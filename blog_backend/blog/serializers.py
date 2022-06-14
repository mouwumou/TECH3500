from datetime import timedelta
from hashlib import blake2b
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import BlogType, Blog

User = get_user_model()

class BlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = ("id", "type_name")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class BlogSerializer(serializers.ModelSerializer):
    blog_type = BlogTypeSerializer()
    author = UserSerializer()

    class Meta:
        model = Blog
        fields = ('id','title', 'img', 'content', 'blog_type', 'author','created_time','last_updated_time')
