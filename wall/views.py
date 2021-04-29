from rest_framework import permissions

from base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from base.permissions import IsMemberGroup, IsAuthorEntry, IsAuthorCommentEntry
from .models import Post, Comment
from .serializers import (PostSerializer, CreateCommentSerializer)

class PostView(CreateRetrieveUpdateDestroy):
    """Редактирование записи в группе"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberGroup]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthorEntry],
                                    'destroy': [IsAuthorEntry]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsView(CreateUpdateDestroy):
    """Редактирование комментариев к запси"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMemberGroup]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthorCommentEntry],
                                    'destroy': [IsAuthorCommentEntry]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()