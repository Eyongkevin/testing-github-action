from django.urls import path
from . import views

app_name = "resources"
urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("resource/<int:id>", views.resource_detail, name="resource-detail"),
    path("resource/post/", views.post_resource, name="post-resource"),
]
