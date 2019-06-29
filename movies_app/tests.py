from django.test import TestCase
import datetime
from .utils import str_to_date, resp_str_to_movie_object
from .models import Movie
from .rest_client import OmdbClient


class UtilsTest(TestCase):

    def setUp(self) -> None:
        self.DATE_STR = '23 Jun 1989'
        self.DATE_OBJ = datetime.date(year=1989, month=6, day=23)
        self.RESPONSE_BATMAN = '{"Title":"Batman","Year":"1989","Rated":"PG-13","Released":"23 Jun 1989","Runtime":"126 ' \
                               'min","Genre":"Action, Adventure","Director":"Tim Burton","Writer":"Bob Kane ' \
                               '(Batman characters), Sam Hamm (story), Sam Hamm (screenplay), Warren Skaaren (screenplay)",' \
                               '"Actors":"Michael Keaton, Jack Nicholson, Kim Basinger, Robert Wuhl","Plot":"The Dark Knight ' \
                               'of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal ' \
                               'Joker.","Language":"English, French, Spanish","Country":"USA, UK","Awards":"Won 1 Oscar. ' \
                               'Another 8 wins & 26 nominations.",' \
                               '"Poster":"https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2.' \
                               '_V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.6/10"},{"Source":' \
                               '"Rotten Tomatoes","Value":"71%"},{"Source":"Metacritic","Value":"69/100"}],"Metascore":"69",' \
                               '"imdbRating":"7.6","imdbVotes":"313,177","imdbID":"tt0096895","Type":"movie","DVD":"25 Mar 1997",' \
                               '"BoxOffice":"N/A","Production":"Warner Bros. Pictures","Website":"N/A","Response":"True"}'

    def tearDown(self) -> None:
        pass

    def test_str_to_date(self):
        self.assertIsInstance(str_to_date(self.DATE_STR), datetime.date)
        self.assertEqual(str_to_date(self.DATE_STR), self.DATE_OBJ)

    def test_resp_str_to_movie_object(self):
        self.assertTrue(resp_str_to_movie_object(self.RESPONSE_BATMAN))
        self.assertIsInstance(resp_str_to_movie_object(self.RESPONSE_BATMAN), Movie)
        self.assertEqual(resp_str_to_movie_object(self.RESPONSE_BATMAN).title, 'Batman')
        self.assertEqual(resp_str_to_movie_object(self.RESPONSE_BATMAN).year, 1989)
        self.assertEqual(resp_str_to_movie_object(self.RESPONSE_BATMAN).released,
                         datetime.date(year=1989, month=6, day=23))
        self.assertEqual(resp_str_to_movie_object(self.RESPONSE_BATMAN).genre, 'Action, Adventure')


class OmdbClientTest(TestCase):

    def setUp(self) -> None:
        self.client = OmdbClient()
        self.movie = self.client.get_movie_by_title('batman')
        pass

    def tearDown(self) -> None:
        pass

    def test_get_movie_by_title(self):
        self.assertIsInstance(self.movie, Movie)
        self.assertEqual(self.movie.title, 'Batman')
        self.assertEqual(self.movie.year, 1989)
        self.assertEqual(self.movie.released,
                         datetime.date(year=1989, month=6, day=23))
        self.assertEqual(self.movie.genre, 'Action, Adventure')
        pass
