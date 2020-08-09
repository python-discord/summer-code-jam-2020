from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from .serializers import BoardSerializer, PostSerializer, CommentSerializer
from .models import Board, Post, Comment


# Create your views here.

class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all().order_by('board')
    serializer_class = BoardSerializer
    lookup_field = 'id'

    @action(detail=True, url_path='posts')
    def get_posts(self, request, id=None):
        """
        Returns the 10 latest posts posted to board with id
        :param request: Request object
        :param id: The id of the board
        :type id: int
        :return: Paginator of the most recent posts
        """
        post_objects = Post.objects.all().filter(board__exact=id).order_by('-publication_date')
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(post_objects, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-publication_date')
    serializer_class = PostSerializer

    @action(detail=True, url_path='comments')
    def get_comments(self, request, pk=None):
        """
        Returns the 10 latest comments commented on post with pk
        :param request: Request object
        :param pk: Primary key of the post
        :return: Paginator of the most recent comments
        """
        comment_objects = Comment.objects.all().filter(post__exact=pk).order_by('-publication_date')
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(comment_objects, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-publication_date')
    serializer_class = CommentSerializer
