from django.apps import AppConfig


class AdminProfileConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'admin_profile'

	def ready(self):
		from .admin_signals import make_row_seats
