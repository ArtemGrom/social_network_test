from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import FanSerializer
from .services import add_like, get_fans, remove_like


class LikedMixin:
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        obj = self.get_object()
        add_like(obj, request.user)

        return Response()

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        remove_like(obj, request.user)

        return Response()

    @action(detail=True, methods=['get'])
    def get_fans(self, request, pk=None):
        obj = self.get_object()
        fans = get_fans(obj)
        serializer = FanSerializer(fans, many=True)

        return Response(serializer.data)
