from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("async/", views.async_view, name="async"),
]
