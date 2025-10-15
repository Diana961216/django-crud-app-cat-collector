from django.urls import path
from . import (
    views,
)  # import views from the current directory, views are similar to controllers in MVC

urlpatterns = [
    # functions based views
    path("", views.home, name="home"),  # root route
    path("about/", views.about, name="about"),  # about route
    path("cats/", views.cat_index, name="cat-index"),  # index route
    path("cats/<int:cat_id>/", views.cat_detail, name="cat-detail"),  # detail route
    # class based view for creating a cat
    path("cats/create/", views.CatCreate.as_view(), name="cat-create"),  # create route
    path(
        "cats/<int:pk>/update/", views.CatUpdate.as_view(), name="cat-update"
    ),  # update route
    path(
        "cats/<int:pk>/delete/", views.CatDelete.as_view(), name="cat-delete"
    ),  # delete route
]
