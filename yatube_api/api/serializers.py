from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CreateOnlyDefault('')
    )

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)

        if 'group' in self.initial_data:
            group = self.initial_data['group']
            post.group = Group.objects.get(pk=group)
            post.save()

        return post

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        return instance
