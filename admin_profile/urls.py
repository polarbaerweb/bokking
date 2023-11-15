from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (delete_session, get_data_by_name,
                    get_data_by_name_and_related_obj, save_data,
                    session_filter, session_template)

app_name = "admin_profile"

urlpatterns = [
	path("", save_data, name="admin"),
	path("save/", save_data, name="save_data"),
	path("get_data_by_name/<str:name>/", get_data_by_name, name="save_data"),
	path("session_list/", session_template, name="session_list"),
	path("session_list/filter/", session_filter, name="filter"),
	path("session_list/get_data_by_name_and_related_obj/<int:cinema_id>/", get_data_by_name_and_related_obj, name="filter"),
	path("delete_session/<int:session_id>", delete_session, name="delete_session"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
