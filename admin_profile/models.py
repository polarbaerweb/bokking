from django.db import models
from django.utils.timezone import now

from show_data import models as md


class Cinema(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return str(self.name)


class Session(models.Model):
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, related_name="sessions"
    )
    hall = models.ForeignKey(
        "Hall", on_delete=models.CASCADE, related_name="sessions")
    movie = models.ForeignKey(
        md.Movie, on_delete=models.CASCADE, related_name="sessions"
    )

    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_vip = models.BooleanField(default=False)

    @property
    def is_not_expired(self):
        return self.start_time > now()

    def __str__(self):
        return f"{self.movie.name} - {self.start_time}"


class Hall(models.Model):
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, related_name="halls")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cinema.name} - {self.name}"


class Row(models.Model):
    hall = models.ForeignKey(
        "Hall", on_delete=models.CASCADE, related_name="rows")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.hall.name} - {self.name}"


class Seat(models.Model):
    row = models.ForeignKey(
        "Row", on_delete=models.CASCADE, related_name="seats")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Seat {self.name} in Row {self.row}"
