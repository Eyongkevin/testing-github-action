from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_users, name="list-users"),
    path("login/", views.login_view, name="login-view"),
    path("profile/", views.profile, name="profile"),
]
