import requests
import os
from .models import Movie
from .utils import resp_str_to_movie_object

KEY = os.environ.get('OMDB_API_KEY')

class OmdbClient:

    @staticmethod
    def get_movie_by_title(title: str) -> Movie:
        title = title.strip()
        response = requests.get(f'http://www.omdbapi.com/?apikey={KEY}&t={title}')
        if "Movie not found!" in str(response.content):
            return None
        return resp_str_to_movie_object(response.content)
