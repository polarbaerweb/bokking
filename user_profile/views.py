from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect, render

from admin_profile import models as admin_md
from user_auth import models as user_auth_md

from . import models as user_md


def get_profile(request, user_id:int=None):
	template_name = "profile.html" if not user_id else "user_profile.html"
	tickets = request.user.ticket.all()
	user = user_auth_md.UserModel.objects.get(id=user_id) if user_id else {}


	context = {
		"tickets": tickets,
		"user": user
	}

	return render(request, template_name, context)


def choose_seats(request, session_id):
	session = get_object_or_404(admin_md.Session, id=session_id)
	hall = session.hall
	rows = admin_md.Row.objects.filter(hall=hall).prefetch_related("seats")

	bookings = user_md.Booking.objects.filter(session=session)
	booked_seats = admin_md.Seat.objects.filter(bookings__in=bookings).values_list(
			"id", flat=True
	)

	context = {
			"session": session,
			"hall": hall,
			"rows": rows,
			"booked_seats": booked_seats,
	}

	return render(request, "choice_seats.html", context)


def book_seat(request, session_id):
	if request.method != "POST":
		return redirect("user_profile:choose_seats", session_id=session_id)

	selected_seats = request.POST.getlist("seat")
	seat_length = len(selected_seats)

	if not selected_seats:
		return redirect("user_profile:choice_seats", session_id=session_id)

	session = get_object_or_404(admin_md.Session, id=session_id)
	user = None

	if request.user.is_authenticated:
		user = request.user
	
	else:
		email = request.POST.get("email")
		username = request.POST.get("username")
		password = request.POST.get("password")
		
		if username and email:
			user = user_auth_md.UserModel(
				email=email,
				username=username,
				password=make_password(password)
			)

			user.save()
		else:
			return redirect("choice_seats", args={"session__id": session_id})
	
	booking = user_md.Booking(session=session, username=user.username)
	booking.save()

	booking.seats.add(*selected_seats)

	price = session.price * seat_length

	ticket = user_md.Ticket(
		user=user,
		booking=booking,
		price=price
	)

	ticket.save()

	if not request.user.is_authenticated:
		return redirect("user_auth:login")

	return redirect("user_profile:profile")