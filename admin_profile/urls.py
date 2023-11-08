from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "admin_profile"

urlpatterns = [
    path("", views.save_data, name="admin"),
    path("save/", views.save_data, name="save_data"),
    path("get_data_by_name/<str:name>/", views.get_data_by_name, name="save_data"),
		path("session_list/", views.session_list, name="session_list"),
		path("delete_session/<int:session_id>", views.delete_session, name="delete_session")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
