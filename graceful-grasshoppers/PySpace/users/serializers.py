from rest_framework import serializers
from . import models
import posts.models as post_models
import posts.serializers as post_serializers
import api.models as api_models
import api.serializers as api_serializers


class ProfileCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("username")

    def username(self, obj):
        return obj.user_commented.username

    class Meta:
        model = models.ProfileComment
        fields = (
            "user",
            "content",
        )


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = (
            "id",
            "username",
        )


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField('user_posts')
    latest_post = serializers.SerializerMethodField('most_recent_post')
    friends = serializers.SerializerMethodField('friend_list')
    profile_comments = serializers.SerializerMethodField('comments')
    profile_picture = serializers.SerializerMethodField('picture')

    def picture(self, obj):
        return api_models.File.objects.get(id=obj.profile_picture.id).file.name

    def friend_list(self, obj):
        queryset = [i.friend_id for i in models.Friendship.objects.filter(requester_id=obj.id)]
        queryset += [i.requester_id for i in models.Friendship.objects.filter(friend_id=obj.id)]
        queryset = [models.CustomUser.objects.get(id=i) for i in queryset]
        return FriendshipSerializer(queryset, many=True).data

    def user_posts(self, obj):
        serializer = post_serializers.PostSerializer(post_models.Post.objects.filter(author=obj.id), many=True)
        return serializer.data

    def most_recent_post(self, obj):
        queryset = post_models.Post.objects.filter(author=obj.id).order_by("date_posted").first()
        serializer = post_serializers.PostSerializer(queryset,)
        return serializer.data

    def comments(self, obj):
        queryset = models.ProfileComment.objects.filter(user_commented_on=obj.id)
        return ProfileCommentSerializer(queryset, many=True).data

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
            'profile_comments',
            'profile_picture',
        )
