from rest_framework import serializers
from . import models
import posts.models as post_models
import posts.serializers as post_serializers


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friendship
        fields = (
            'requester',
            'friend',
        )


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField('user_posts')
    latest_post = serializers.SerializerMethodField('most_recent_post')
    friends = serializers.SerializerMethodField('friend_list')

    def friend_list(self, obj):
        queryset = models.Friendship.objects.all()
        print(queryset)
        return FriendshipSerializer(queryset, many=True).data

    def user_posts(self, obj):
        serializer = post_serializers.PostSerializer(
            post_models.Post.objects.filter(author=obj.id),
            many=True
        )
        return serializer.data

    def most_recent_post(self, obj):
        queryset = post_models.Post.objects.filter(author=obj.id).order_by('date_posted').first()
        serializer = post_serializers.PostSerializer(queryset,)
        return serializer.data

    class Meta:
        model = models.CustomUser
        fields = (
            'id',
            'email',
            'username',
            'about',
            'name',
            'age',
            'posts',
            'latest_post',
            'friends',
        )
