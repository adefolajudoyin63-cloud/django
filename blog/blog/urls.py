from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

=======
from django.urls import path
from django.urls.conf import include 
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217

# Import views from the django_project app
from django_project.views import (
    homepage,
    article,
    blog_post, 
    not_found,
<<<<<<< HEAD
    edit_blog,
    register,
    profile,
    delete_blog
=======
    delete_blog,
    edit_blog,
    register,
    login,
    my_blogs
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
)
from django.contrib.auth.models import User


urlpatterns = [
    # Django admin site
    path("admin/", admin.site.urls),

<<<<<<< HEAD
    path("accounts/", include('django.contrib.auth.urls')),

    path("accounts/register", register, name="register"),

    # Home page (added name='home')
    path("", homepage, name="home"),

=======
    # Login and signup pages (registered before the auth include
    path("accounts/login/", login, name="login"),

    path("accounts/signup/", register, name="signup"),

    #accounts
    path("accounts/", include('django.contrib.auth.urls')),

    # Home page (added name='home')
    path("", homepage, name="home"),

    # About page
    path("about/", about, name="about"),

    #userblogs
    path("my_blogs/", my_blogs, name="my_blogs"),

>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
    # Article page (added trailing slash)
    path("article/<int:pk>/", article, name="article"),

    # Create blog page
    path("create_blog/", blog_post, name="create_blog"),

    # Page not found
    path("not_found/", not_found, name="not_found"),

    #edit
    path("article/<int:pk>/edit/", edit_blog, name = "edit_blog"),

     #profile
     path("accounts/profile", profile, name= "profile"),

    #delete
<<<<<<< HEAD
    path("article/<int:pk>/delete/", delete_blog, name = "delete_blog")


=======
    path("article/<int:pk>/delete/", delete_blog, name = "delete_blog"),

    #edit
    path("article/<int:pk>/edit/", edit_blog, name="edit_blog")
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
]

# Catches any missed or invalid route across your entire project:
# handler404 = "django_project.views.not_found"