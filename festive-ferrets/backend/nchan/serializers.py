# serializers.py
from rest_framework import serializers

from .models import Board, Post, Comment


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'board', 'title')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'board', 'poster', 'publication_date', 'text')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'commenter', 'publication_date', 'text')
