from rest_framework import serializers
from users.models import Account

User = Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "number_of_posts",
            "number_of_likes",
            "number_of_comments",
            "number_of_messages",
            "score",
        ]
