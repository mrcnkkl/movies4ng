from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .utils import *
from django.db.models import ObjectDoesNotExist
from .rest_client import OmdbClient
from .models import Movie, MovieComment
from .serializers import MovieSerializer, MovieCommentSerializer, TopCommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        title = request.data['title']
        movie_qs = Movie.objects.filter(title__iexact=title.strip())
        if not movie_qs:
            # TODO: Exception handling
            fetched_movie = OmdbClient.get_movie_by_title(title)
            if not fetched_movie:
                return Response({"Response": False, "Error": "Movie not found!"}, status=status.HTTP_204_NO_CONTENT)
            else:
                fetched_movie.save()
                serializer = MovieSerializer(fetched_movie, many=False)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        else:
            movie = movie_qs.first()
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)


class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id', None)
        if movie_id:
            comments = MovieComment.objects.filter(movie=movie_id)
        else:
            comments = MovieComment.objects.all()
        return comments

    def create(self, request, *args, **kwargs):
        movie_id = request.data['movie_id']
        try:
            movie = Movie.objects.get(pk=movie_id)
        except ObjectDoesNotExist:
            return Response({"error": f"No movie with id: {movie_id}"})
        movie.total_comments += 1
        movie.save()
        comment = MovieComment.create(content=request.data['content'], movie=movie)
        comment.save()
        serializer = MovieCommentSerializer(comment, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopCommentViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        return Response(group_by_comm_quant(queryset), status=status.HTTP_200_OK)
