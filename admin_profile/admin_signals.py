"""
This module assists us with adding necessary thing when data 
was added with the help of built in admin panel
"""

import logging

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models as md

Logger = logging.getLogger(__name__)


@receiver(post_save, sender=md.Cinema)
def make_halls_rows_seats(sender, instance, created, **kwargs):
	"""This function will generate halls, rows, seats for cinema"""

	if created:
		hall_id = 1
		hall_name = "hall{hall_num}"

		try:
				hall_id = md.Hall.objects.latest("id").id
				hall_name.format(hall_num=hall_id)

		except (IntegrityError, ObjectDoesNotExist) as error:
				Logger.error(f"An error occurred {str(error)}")
				hall_name.format(hall_num=1)

		finally:
				hall = md.Hall.objects.create(cinema=instance, name=f"hall{hall_id}")

		for row_num in range(5):
				row = md.Row.objects.create(hall=hall, name=f"row{row_num}")

				for seat_num in range(5):
						seat = md.Seat.objects.create(row=row, name=f"seat{seat_num}")


@receiver(post_save, sender=md.Hall)
def make_rows_seats(sender, instance, created, **kwargs):
	"""This function will generate rows, seats for halls"""

	if created:
		for row_num in range(5):
			row = md.Row.objects.create(hall=instance, name=f"row{row_num}")

			for seat_num in range(5):
					seat = md.Seat.objects.create(row=row, name=f"seat{seat_num}")