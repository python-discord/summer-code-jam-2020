from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from random import choice

# Create your views here.


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """Optionally restricts the returned users to a given user
        by filtering against a `username` query parameter in the URL"""
        queryset = models.CustomUser.objects.all()
        username = self.request.query_params.get("username", None)
        random_param = self.request.query_params.get("random", None)
        if random_param is not None:
            print(queryset)
            random_user_id = choice([user.id for user in queryset])
            queryset = models.CustomUser.objects.filter(id=random_user_id)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class LoggedInUserView(APIView):
    """Returns information about currently logged in user"""

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        print(user)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def comment_on_profile(request):
    """Creates a post with the authenticated user as the author"""
    payload = request.data
    user = request.user
    try:
        comment = models.ProfileComment.objects.create(
            user_commented_on=models.CustomUser.objects.get(username=payload["user_commented_on"]),
            user_commented=models.CustomUser.objects.get(id=user.id),
            content=payload["content"],
        )
        print(comment)
        serializer = serializers.ProfileCommentSerializer(comment)
        return JsonResponse({"comment": serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        print(e)
        return JsonResponse({"error": str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse(
            {"error": "Something went terribly wrong!"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
