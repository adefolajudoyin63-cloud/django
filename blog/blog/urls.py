from django.contrib import admin
from django.urls import include, path

from django_project.views import (
    about,
    article,
    blog_post,
    delete_blog,
    edit_blog,
    homepage,
    my_blogs,
    not_found,
    profile,
    register,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="home"),
    path("about/", about, name="about"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", register, name="register"),
    path("accounts/signup/", register, name="signup"),
    path("accounts/profile/", profile, name="profile"),
    path("article/<int:pk>/", article, name="article"),
    path("article/<int:pk>/edit/", edit_blog, name="edit_blog"),
    path("article/<int:pk>/delete/", delete_blog, name="delete_blog"),
    path("create_blog/", blog_post, name="create_blog"),
    path("my_blogs/", my_blogs, name="my_blogs"),
    path("not_found/", not_found, name="not_found"),
]

# Catches any missed or invalid route across your entire project:
# handler404 = "django_project.views.not_found"