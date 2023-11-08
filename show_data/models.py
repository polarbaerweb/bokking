from django.db import models

from actors import models as actor_model


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            null=False, default="undecided")
    name_translated = models.CharField(
        max_length=100, unique=True, null=False, default="undecided")
    summary = models.CharField(max_length=300, default="", null=True)
    description = models.TextField()
    city = models.CharField(max_length=30, default="undecided", null=False)

    img = models.ImageField(upload_to="posters")

    date = models.DateTimeField(auto_now_add=True)

    rating = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField(default=0)

    actors = models.ManyToManyField(actor_model.Actors, related_name="movies")
    genre = models.ManyToManyField('Genre', related_name="movies")

    @property
    def is_max_rating(self) -> bool:
        return self.rating == 10

    def __str__(self):
        return str(self.name)


class Collection(models.Model):
    title = models.CharField(
        max_length=255, default="undecided", unique=True, null=False)

    movie = models.ManyToManyField(Movie, related_name="collection")

    def __str__(self) -> str:
        return str(self.title)


class Genre(models.Model):
    title = models.CharField(
        max_length=30, default="undecided", unique=True, null=False)

    def __str__(self) -> str:
        return str(self.title)
