from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


class AuthManager(BaseUserManager):
    """
    Custom base user manager to make email address of end user unique identifier
    instead of username
    """

    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError(_("You must provide a email address"))

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
