from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=15)
    released = models.DateField(null=True)
    genre = models.CharField(max_length=250)
    total_comments = models.IntegerField(default=0)

    @classmethod
    def create(cls, title, year, released, genre):
        movie = cls(title=title, year=year, released=released, genre=genre)
        return movie

    def __str__(self):
        return f'Movie(title={self.title}, genre={self.genre}, total_comments={self.total_comments})'

    class Meta:
        ordering = ['total_comments']


class MovieComment(models.Model):
    content = models.CharField(max_length=300)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)

    @classmethod
    def create(cls, content: str, movie: Movie):
        comment = cls(content=content, movie=movie)
        return comment

    def __str__(self):
        return f'MovieComment(movie={self.movie.title}, content={self.content})'