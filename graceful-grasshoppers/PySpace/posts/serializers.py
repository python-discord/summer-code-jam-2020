from rest_framework import serializers
from .models import Post, Dislike, Like, PostComment


class PostCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('username')

    def username(self, obj):
        return obj.user_commented.username

    class Meta:
        model = PostComment
        fields = ("user", "content")


class PostSerializer(serializers.ModelSerializer):
    dislikes = serializers.SerializerMethodField('dislike_count')
    likes = serializers.SerializerMethodField('like_count')
    author = serializers.SerializerMethodField('post_author')
    comments = serializers.SerializerMethodField('post_comments')

    def post_author(self, obj):
        return obj.author.username

    def like_count(self, obj):
        return obj.likes.count()

    def dislike_count(self, obj):
        return obj.dislikes.count()

    def post_comments(self, obj):
        queryset = PostComment.objects.filter(post_id=obj.id)
        return PostCommentSerializer(queryset, many=True).data

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "date_posted", "likes", "dislikes", "comments")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user_liked", "date_liked")


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ("user_disliked", "date_disliked")
