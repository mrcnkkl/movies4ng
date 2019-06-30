import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie
from .serializers import MovieSerializer

client = Client()


class MovieApiTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_movie_post(self):
        response = client.post(
            path='/movies/',
            data=json.loads('{"title":"The Lord of the Rings: The Fellowship of the Ring"}'),
            content_type='application/json'
        )
        self.assertTrue("The Lord of the Rings: The Fellowship of the Ring" in str(response.content))