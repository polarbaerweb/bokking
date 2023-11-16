from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from .manager import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, max_length=254)
	
	username = models.CharField(max_length=255, default="", unique=True, verbose_name=_("User name"))
	first_name = models.CharField(max_length=20, null=True)
	last_name = models.CharField(max_length=20, null=True)
	user_address = models.CharField(max_length=40, default="Address is not indicated", null=False, verbose_name=_("User address"))
	
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	
	user_image = models.ImageField(upload_to="user_images/", null=True)

	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = ["email"]

	objects = UserManager()

	def __str__(self):
		return str(self.email)
