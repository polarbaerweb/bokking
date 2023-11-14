from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "admin_profile"

urlpatterns = [
	path("", views.save_data, name="admin"),
	path("save/", views.save_data, name="save_data"),
	path("get_data_by_name/<str:name>/", views.get_data_by_name, name="save_data"),
	path("session_list/", views.session_template, name="session_list"),
	path("session_list/filter/", views.session_filter, name="filter"),
	path("session_list/get_data_by_name_and_related_obj/<int:cinema_id>/", views.get_data_by_name_and_related_obj, name="filter"),
	path("delete_session/<int:session_id>", views.delete_session, name="delete_session"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
