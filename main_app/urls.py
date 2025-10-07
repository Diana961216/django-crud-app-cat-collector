from django.urls import path
from . import (
    views,
)  # import views from the current directory, views are similar to controllers in MVC

urlpatterns = [
    path("", views.home, name="home"),  # root route
    path("about/", views.about, name="about"),  # about route
    path("cats/", views.cats_index, name="cat-index"),  # index route
]
