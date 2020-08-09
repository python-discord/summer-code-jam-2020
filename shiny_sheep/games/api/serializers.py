from rest_framework import serializers

from shiny_sheep.games.models import Room
from shiny_sheep.users.models import User


class RoomSerializer(serializers.ModelSerializer):
    """The JSON Serializer for the Room model"""

    class Meta:
        model = Room
        fields = ['name', 'owner', 'average_rating', 'game_type', 'game_id']
        read_only_fields = ['name', 'owner', 'average_rating', 'game_type', 'game_id']

    def validate_average_rating(self, value):
        """Check to see if the rating is between 1 and 5"""
        if not 1 <= value <= 5:
            raise serializers.ValidationError('average_rating is not between 1 and 5')
        return value

    def create(self, validated_data):
        validated_data['owner'] = User.objects.filter(username=validated_data['owner']).first()
        return Room.objects.create(**validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = instance.owner.username
        return ret
