from asyncore import read
from dataclasses import fields
from rest_framework import serializers


from .models import Post, Comment, Complaint


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'caption', 'is_active', 'is_public')
        extra_kwargs = {
            'user' : {'read_only' : True}
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('post', 'user', 'text', 'suggested_price')
        extra_kwargs = {
            'post':{'read_only': True},
            'user':{'read_only': True},
            'is_liked':{'required': False},
        }


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields =('post', 'user', 'txt')
        extra_kwargs = {
            'post':{'read_only': True},
            'user':{'read_only': True},
        }