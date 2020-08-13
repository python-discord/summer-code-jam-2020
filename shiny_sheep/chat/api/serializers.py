from rest_framework import serializers

from shiny_sheep.chat.models import Room


class RoomSerializer(serializers.ModelSerializer):
    """The JSON Serializer for the Room model"""

    class Meta:
        model = Room
        fields = ['name', 'owner']

    def validate_average_rating(self, value):
        """Check to see if the rating is between 1 and 5"""
        if not 1 <= value <= 5:
            raise serializers.ValidationError('average_rating is not between 1 and 5')
        return value

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = instance.owner.username
        ret['pk'] = instance.pk
        ret['date_created'] = instance.date_created.timestamp()
        return ret
