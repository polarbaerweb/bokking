from django.db import models
from django.contrib.auth.models import AbstractUser

from .auth_model_manager import AuthManager


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    user_image = models.ImageField(upload_to="user_images/")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = AuthManager()

    def __str__(self) -> str:
        return str(self.email)
