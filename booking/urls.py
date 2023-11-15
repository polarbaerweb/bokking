from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("show_data.urls")),
    path("user_auth/", include("user_auth.urls")),
    path("user_admin/", include("admin_profile.urls")),
    path("user_profile/", include("user_profile.urls")),
]
