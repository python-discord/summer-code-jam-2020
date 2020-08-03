from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer

# Create your views here.


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({"posts": serializer.data})


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_post(request):
	pass


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_post(request):
	pass


@api_view(["PATCH"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_post(request):
	pass
