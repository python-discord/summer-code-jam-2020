from rest_framework import serializers
from .models import Post, Dislike, Like


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'content', 'author', 'date_posted')

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Like
		fields = ('user_liked', 'date_liked')

class DislikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dislike
		fields = ('user_disliked', 'date_disliked')
