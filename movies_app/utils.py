from datetime import datetime, date
from .models import Movie
import json

def str_to_date(date_as_string: str) -> date:
    date_object = datetime.strptime(date_as_string, '%d %b %Y').date()
    return date_object


def resp_str_to_movie_object(resp_Str) -> Movie:
    if not resp_Str: return None
    json_obj = json.loads(resp_Str)
    movie = Movie()
    movie.title = json_obj['Title']
    movie.year = int(json_obj['Year'])
    movie.released = str_to_date(json_obj['Released'])
    movie.genre = json_obj['Genre']
    return movie