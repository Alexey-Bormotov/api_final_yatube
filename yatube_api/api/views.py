from django.shortcuts import get_object_or_404
from rest_framework import exceptions, filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Follow, Group, Post, User
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer,
                          FollowSerializer,
                          GroupSerializer,
                          PostSerializer)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def check_post(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)

        return post

    def get_queryset(self):
        post = self.check_post()
        new_queryset = post.comments.all()

        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.check_post())


class FollowViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        new_queryset = user.follower.all()

        return new_queryset

    def perform_create(self, serializer):
        following = get_object_or_404(
            User,
            username=serializer.initial_data['following']
        )

        if following == self.request.user:
            raise exceptions.ValidationError(
                'Подписка на самого себя запрещена.'
            )
        if Follow.objects.filter(
            user=self.request.user,
            following=following
        ).exists():
            raise exceptions.ValidationError('Подписка уже оформлена.')

        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
