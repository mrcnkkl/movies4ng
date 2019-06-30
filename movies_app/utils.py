from datetime import datetime, date
from itertools import groupby
from .models import Movie
import json


def str_to_date(date_as_string: str) -> date:
    try:
        date_object = datetime.strptime(date_as_string, '%d %b %Y').date()
        return date_object
    except ValueError:
        return None


def resp_str_to_movie_object(resp_Str) -> Movie:
    if not resp_Str: return None
    json_obj = json.loads(resp_Str)
    movie = Movie.create(
        title=json_obj['Title'],
        year=json_obj['Year'],
        released=str_to_date(json_obj['Released']),
        genre=json_obj['Genre'])
    return movie


def group_by_comm_quant(queryset):
    movie_list = [movie for movie in queryset]
    KEY = lambda x: x.total_comments
    g = groupby(sorted(movie_list, key=KEY, reverse=True), key=KEY)
    ranked_list = []
    curr_rank = 1
    for _, group in g:
        for movie in group:
            ranked_list.append({
                "movie_id": movie.id,
                "total_comments": movie.total_comments,
                "rank": curr_rank
            })
        curr_rank += 1
    return ranked_list