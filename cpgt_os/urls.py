from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("cpgt_os.urls")),
    path("admin/", admin.site.urls)
]