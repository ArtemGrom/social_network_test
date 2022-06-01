from django.contrib.auth.models import User
from rest_framework import serializers
from . import services as likes_services

from network.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'message', 'author', 'is_fan', 'total_likes')
        read_only_fields = ['date_add']

    def get_is_fan(self, obj) -> bool:
        """Check user like on object.
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'full_name', )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
