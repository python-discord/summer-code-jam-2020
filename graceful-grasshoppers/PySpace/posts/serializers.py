from rest_framework import serializers
from .models import Post, Dislike, Like


class PostSerializer(serializers.ModelSerializer):
    dislikes = serializers.SerializerMethodField('dislike_count')
    likes = serializers.SerializerMethodField('like_count')
    author = serializers.SerializerMethodField('username')

    def username(self, obj):
        return obj.author.username

    def like_count(self, obj):
        return obj.likes.count()

    def dislike_count(self, obj):
        return obj.dislikes.count()

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "date_posted", "likes", "dislikes")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user_liked", "date_liked")


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ("user_disliked", "date_disliked")
