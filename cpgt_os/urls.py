from django.urls import path

from . import views

urlpatterns = [
    path("cpgt_os/", views.index, name="index"),
]