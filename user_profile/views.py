from django.shortcuts import get_object_or_404, redirect, render

from admin_profile import models as admin_md
from user_auth import models as user_auth_md

from . import models as user_md


def get_profile(request):
	template_name = "profile.html"
	tickets = user_md.Ticket.objects.filter(user__email=request.user.email)

	print(tickets)

	context = {
		"tickets": tickets
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

    if not selected_seats:
        return redirect("user_profile:choice_seats", session_id=session_id)

    session = get_object_or_404(admin_md.Session, id=session_id)
    booking = user_md.Booking(session=session, username=request.user.username)
    booking.save()

    booking.seats.add(*selected_seats)

    ticket = user_md.Ticket(
			user=request.user,
			booking=booking
		)
    ticket.save()

    return redirect("user_profile:profile")