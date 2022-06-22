from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import PostSerializer, PostAuthorSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', ]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_class
        elif self.action == "post_author":
            return PostAuthorSerializer
        elif self.action == "all_post_author":
            return PostAuthorSerializer
        else:
            return self.serializer_class

    def retrieve(self, request, pk=None):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path=r'post-author',)
    def post_author(self, request, pk=None):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path=r'all-post-author',)
    def all_post_author(self, request):
        post = Post.objects.all()
        serializer = self.get_serializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)