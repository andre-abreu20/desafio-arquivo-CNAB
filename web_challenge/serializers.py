
import ipdb
from rest_framework.serializers import FileField, Serializer, models

from web_challenge.models import Post


# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField(read_only=True)
    class Meta:
        models = Post
        fields = ["content"]
    def create(self, validated_data):
        # ipdb.set_trace()
        file = Post.objects.create(**validated_data)
        return file
