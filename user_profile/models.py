import uuid

from django.db import models

from admin_profile import models as admin_md
from user_auth import models as user_md


class Booking(models.Model):
	username = models.CharField(max_length=100)
	session = models.ForeignKey(
			admin_md.Session, on_delete=models.CASCADE, related_name="bookings"
	)
	seats = models.ManyToManyField(admin_md.Seat, related_name="bookings")
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
			return f"{self.username} - {self.session} - {self.seats}"


class Ticket(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(user_md.UserModel, on_delete=models.CASCADE, related_name="ticket")
	booking = models.OneToOneField(
			Booking, on_delete=models.CASCADE, related_name="ticket"
	)

	price = models.DecimalField(max_digits=1_000_000, decimal_places=2, default=0, null=False)

	def __str__(self):
			return f"Ticket ID: {self.id}"
