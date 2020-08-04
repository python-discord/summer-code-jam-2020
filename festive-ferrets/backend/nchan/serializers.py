# serializers.py
from rest_framework import serializers

from .models import Board, Post, Comment


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'post_num')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'board', 'poster', 'publication_date', 'text')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'commenter', 'publication_date', 'text')
