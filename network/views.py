from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all().order_by('-date_add')
    serializer_class = PostSerializer
    # authentication_classes = (TokenAuthentication, )
