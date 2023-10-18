from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from .views import movies_list, movies_detail

app_name = "show_data"


urlpatterns = [
	path("", movies_list, name="home"),
	path("detail/<int:movie_id>", movies_detail, name="detail"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
