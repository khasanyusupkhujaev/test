from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registration/", views.registration_view, name="registration"),
    path("menu/", views.photo_feed, name="menu"),
    path("menu/<uid>", views.open_user_view, name="menu1"),
    path("edit/", views.edit_view, name="edit"),
    path("editpic/", views.picture_edit, name="editpic"),
    path("like/", views.like_post, name="likepost"),
    path("search/", views.search_user, name="search_user"),
    path("comment/", views.comment, name="comment"),
]