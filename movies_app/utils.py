from datetime import datetime, date
from .models import Movie
import json


def str_to_date(date_as_string: str) -> date:
    try:
        date_object = datetime.strptime(date_as_string, '%d %b %Y').date()
        return date_object
    except ValueError:
        return 'no data'


def resp_str_to_movie_object(resp_Str) -> Movie:
    if not resp_Str: return None
    json_obj = json.loads(resp_Str)
    movie = Movie.create(
        title=json_obj['Title'],
        year=json_obj['Year'],
        released=str_to_date(json_obj['Released']),
        genre=json_obj['Genre'])
    return movie
