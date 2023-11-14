from django.apps import AppConfig


class AdminProfileConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'admin_profile'

	def ready(self):
		from .admin_signals import make_halls_rows_seats, make_rows_seats
