from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    released = models.DateField(null=True)
    genre = models.CharField(max_length=250)
    total_comments = models.IntegerField(default=0)

    @classmethod
    def create(cls,title, year, released, genre):
        movie = cls(title=title, year=year, released=released, genre=genre)
        return movie

    class Meta:
        ordering = ['total_comments']




class MovieComment(models.Model):
    content = models.CharField(max_length=300)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
