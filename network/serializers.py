from rest_framework import serializers

from network.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['date_add']
