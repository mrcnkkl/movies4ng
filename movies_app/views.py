from django.forms.models import model_to_dict
from .models import Movie, MovieComment
from rest_framework import viewsets
from .serializers import MovieSerializer, MovieCommentSerializer, TopCommentSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import *
from .rest_client import OmdbClient


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        title = request.data['title']
        movie_qs = Movie.objects.filter(title__iexact=title.strip())
        if not movie_qs:
            #TODO: Exception handling
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

    # def list(self, request, *args, **kwargs):
    #     import pdb; pdb.set_trace()

    # def retrieve(self, request, *args, **kwargs):
    #     import pdb; pdb.set_trace()


class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer


class TopCommentViewSet(viewsets.ModelViewSet):
    # queryset = MovieComment.objects.filter(id=1)
    serializer_class = TopCommentSerializer

    def get_queryset(self):
        queryset = MovieComment.objects.all().filter(id=1)
        return queryset
