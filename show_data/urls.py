from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import get_genre_by_id, get_genre_list, movies_detail, movies_list

app_name = "show_data"


urlpatterns = [
	path("", movies_list, name="home"),
	path("detail/<int:movie_id>", movies_detail, name="detail"),
	path("genre_list/", get_genre_list, name="genre_list"),
	path("genre/<int:genre_id>", get_genre_by_id, name="genre_by_id"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
