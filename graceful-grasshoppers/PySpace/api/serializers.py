from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField('file_name')

    def file_name(self, obj):
    	return obj.file.name

    class Meta:
        model = File
        fields = ("filename")
