from rest_framework import serializers
from .models import Movie
from .models import MovieComment


class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = ('id', 'content', 'movie')


class MovieSerializer(serializers.ModelSerializer):
    comments = MovieCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'released', 'genre', 'total_comments', 'comments')


class TopCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = ('id', 'content', 'movie')
