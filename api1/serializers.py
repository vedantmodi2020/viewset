from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from .models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class PostAuthorSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'Author_Name', )