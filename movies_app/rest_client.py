import requests
import os
from .models import Movie
from .utils import resp_str_to_movie_object

KEY = os.environ.get('OMDB_API_KEY')

class OmdbClient:

    def __init__(self):
        self.key = os.environ.get('OMDB_API_KEY')

    @staticmethod
    def get_movie_by_title(self, title:str) -> Movie:
        title = title.strip()
        response = requests.get(f'http://www.omdbapi.com/?apikey={KEY}&t={title}')
        return resp_str_to_movie_object(response.content)
