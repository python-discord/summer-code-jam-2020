from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Like, Dislike
from .serializers import PostSerializer, DislikeSerializer, LikeSerializer
from users.models import CustomUser

# Create your views here.


@api_view(["GET"])
@csrf_exempt
def get_posts(request):
    """Returns a list of posts, can be restricted to a particular
    user via the `user` query parameter"""

    posts = Post.objects.all()
    user_id = request.query_params.get("user", None)
    post_id = request.query_params.get("post", None)
    username = request.query_params.get("username", None)

    if user_id is not None:
        posts = posts.filter(author=user_id)
    if post_id is not None:
        posts = posts.filter(id=post_id)
    if username is not None:
        user = CustomUser.objects.get(username=username)
        posts = posts.filter(author_id=user.id)

    serializer = PostSerializer(posts, many=True)
    response = {"posts": serializer.data, "liked_posts": []}

    if request.user.is_authenticated:
        for i, post in enumerate(posts):
            if post.likes.filter(user_liked=request.user).count() > 0:
                response["liked_posts"].append(i)

    return JsonResponse(response)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_post(request):
    """Creates a post with the authenticated user as the author"""
    payload = request.data
    user = request.user
    try:
        author = CustomUser.objects.get(id=user.id)
        post = Post.objects.create(title=payload["title"], content=payload["content"], author=author,)
        serializer = PostSerializer(post)
        return JsonResponse({"books": serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went terribly wrong!"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    """Deletes the post with the given post id"""
    user = request.user
    try:
        post = Post.objects.get(id=post_id, author=user.id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong!"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["PATCH"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    """Given a post id, updates the post with given data"""
    payload = request.data
    user = request.user
    try:
        post_item = Post.objects.filter(id=post_id, author=user.id)
        post_item.update(**payload)  # returns 0 or 1
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return JsonResponse({"post": serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    """Adds a like to a post attributed to the authenticated user"""
    user = request.user
    try:
        post = Post.objects.get(id=post_id)

        # Check if the user has previously disliked the post, if so, remove the dislike
        dislikes = post.dislikes.filter(user_disliked=user.id)
        for dislike in dislikes:
            dislike.delete()

        # Don't go any further if the user has already liked this post
        likes = post.likes.filter(user_liked=user.id)
        if likes.count() > 0:
            return JsonResponse({"posts": None}, safe=False, status=status.HTTP_200_OK)

        like = Like(user_liked=user)
        like.save()
        post.likes.add(like)

        serializer = LikeSerializer(like, many=True)
        return JsonResponse({"posts": serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def dislike_post(request, post_id):
    """Adds a dislike to a post attributed to the authenticated user"""
    user = request.user
    try:
        post = Post.objects.get(id=post_id)

        # Check if the user has previously liked the post, if so, remove the like
        likes = post.likes.filter(user_liked=user.id)
        for like in likes:
            like.delete()

        # Don't go any further if the user has already disliked this post
        dislikes = post.dislikes.filter(user_disliked=user.id)
        if dislikes.count() > 0:
            return JsonResponse({"posts": None}, safe=False, status=status.HTTP_200_OK)

        dislike = Dislike(user_disliked=user)
        dislike.save()
        post.dislikes.add(dislike)

        serializer = DislikeSerializer(dislike, many=True)
        return JsonResponse({"posts": serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went wrong"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
