# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ["id", "text", "timestamp", "user"]

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "text", "timestamp", "user", "comment_count", "comments"]

    def get_comments(self,obj):
        # To fetch 3 random comments instead of latest
        qs = obj.comments.all().order_by("-timestamp")[:3]
        return CommentSerializer(qs, many=True).data

    def get_comment_count(self,obj):
        return obj.comments.count() 

