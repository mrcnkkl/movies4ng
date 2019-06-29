from django.shortcuts import render
from .models import Movie, MovieComment
from rest_framework import viewsets
from .serializers import MovieSerializer, MovieCommentSerializer, TopCommentSerializer
from rest_framework.response import Response
from rest_framework import status


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        title = request.data['title']


    # def create(self, request, *args, **kwargs):
    #     print(f'\n\n-------------------------------------------------\n ')
    #     print(f'\n\n\n {request.data}\n\n\n')
    #     print(f'\n-----------------------------------------------------\n\n')
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        d = {'error':'dupa', 'message':'dupa2'}
        return Response(d, status=status.HTTP_201_CREATED)





class MovieCommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = MovieCommentSerializer


class TopCommentViewSet(viewsets.ModelViewSet):
    # queryset = MovieComment.objects.filter(id=1)
    serializer_class = TopCommentSerializer

    def get_queryset(self):
        queryset = MovieComment.objects.all().filter(id=1)
        return queryset

