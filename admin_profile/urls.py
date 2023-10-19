from django.urls import path

from . import views

app_name = "admin_profile"

urlpatterns = [
	path("", views.save_data, name="admin"),
	path("save/", views.save_data, name="save_data"),
]
