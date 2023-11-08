from django.db import models


class Actors(models.Model):
    first_name = models.CharField(
        max_length=20, default="undecided", null=False)
    last_name = models.CharField(
        max_length=20, default="undecided", null=False)
    sure_name = models.CharField(
        max_length=20, default="undecided", null=False)

    prizes = models.ManyToManyField("Prizes", related_name="actors")
    jobs = models.ManyToManyField("Jobs", related_name="actors")

    def __str__(self) -> str:
        return str(self.id)


class Prizes(models.Model):
    name = models.CharField(max_length=20, default="undecided", null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Jobs(models.Model):
    name = models.CharField(max_length=40, default="",
                            null=False, unique=True)

    def __str__(self) -> str:
        return str(self.name)
