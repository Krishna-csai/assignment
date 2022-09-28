from rest_framework import serializers
from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'intro', 'body', 'date_added']