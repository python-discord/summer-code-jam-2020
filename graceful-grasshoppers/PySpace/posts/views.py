from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .serializers import PostSerializer
from users.models import CustomUser

# Create your views here.


@api_view(["GET"])
@csrf_exempt
def get_posts(request):
    posts = Post.objects.all()
    user_id = request.query_params.get('user', None)
    if user_id is not None:
        posts = posts.filter(author=user_id)
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({"posts": serializer.data})


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_post(request):
    payload = request.data
    user = request.user
    try:
        author = CustomUser.objects.get(id=user.id)
        post = Post.objects.create(
            title=payload["title"], content=payload["content"], author=author,
        )
        serializer = PostSerializer(post)
        return JsonResponse(
            {"books": serializer.data}, safe=False, status=status.HTTP_201_CREATED
        )
    except ObjectDoesNotExist as e:
        return JsonResponse(
            {"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND
        )
    except Exception:
        return JsonResponse(
            {"error": "Something went terribly wrong!"},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


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
