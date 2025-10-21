from django.urls import path
from . import (
    views,
)  # import views from the current directory, views are similar to controllers in MVC

urlpatterns = [
    # functions based views
    path("", views.Home.as_view(), name="home"),  # root route
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
    path(
        "cats/<int:cat_id>/add_feeding/", views.add_feeding, name="add-feeding"
    ),  # add feeding route for a specific cat
    path("toys/create/", views.ToyCreate.as_view(), name="toy-create"),
    path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toy-detail"),
    path("toys/", views.ToyList.as_view(), name="toy-index"),
    path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toy-update"),
    path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toy-delete"),
    path(
        "cats/<int:cat_id>/assoc_toy/<int:toy_id>/",
        views.associate_toy,
        name="associate-toy",
    ),
    path(
        "cats/<int:cat_id>/remove-toy/<int:toy_id>/",
        views.remove_toy,
        name="remove-toy",
    ),
    # user signup route
    path("accounts/signup/", views.signup, name="signup"),
]
