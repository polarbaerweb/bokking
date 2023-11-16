from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import book_seat, choose_seats, get_profile

app_name = "user_profile"

urlpatterns = [
	path("profile/", get_profile, name="profile"),
	path("profile/<int:user_id>", get_profile, name="profile"),
	path("choice_seats/<int:session_id>", choose_seats, name="choice_seats"),
	path("book_seat/<int:session_id>", book_seat, name="book_seat"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL + settings.SEAT_IMAGES_DIR, document_root=settings.SEAT_IMAGES_ROOT)