from django.urls import path
from . import (
    views,
)  # import views from the current directory, views are similar to controllers in MVC

urlpatterns = [
    path("", views.home, name="home"),  # root route
    path("about/", views.about, name="about"),  # about route
    path("cats/", views.cat_index, name="cat-index"),  # index route
    path("cats/<int:cat_id>/", views.cat_detail, name="cat-detail"),  # detail route
]
