import json
from django.test import TestCase, Client

client = Client()


class MovieApiTest(TestCase):

    def test_movie_post(self):
        response = client.post(
            path='/movies/',
            data=json.loads('{"title":"The Lord of the Rings: The Fellowship of the Ring"}'),
            content_type='application/json'
        )
        self.assertTrue("The Lord of the Rings: The Fellowship of the Ring" in str(response.content))

    def test_comment_post(self):
        client.post(
            path='/movies/',
            data=json.loads('{"title":"The Lord of the Rings: The Fellowship of the Ring"}'),
            content_type='application/json'
        )
        response = client.post(
            path='/comments/',
            data=json.loads('{"content": "comment", "movie_id": 1}'),
            content_type='application/json'
        )
        self.assertTrue("comment" in str(response.content))
