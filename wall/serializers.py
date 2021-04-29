from rest_framework import serializers

from backend.api.v2.viewsets.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """Добавление комментариев к посту"""
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """Список комментариев"""
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "text", "created_date", "update_date", "deleted", "children")


class PostSerializer(serializers.ModelSerializer):
    """Вывод и редактирование поста"""
    user = serializers.ReadOnlyField(source='user.username')
    comment = ListCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", 'view_count', "text", "comment")


class ListPostSerializer(serializers.ModelSerializer):
    """Список  постов"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "create_date", "user", "text", "comments_count")

