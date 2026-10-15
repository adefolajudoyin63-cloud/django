from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BlogForm
from .models import Blog


def homepage(request):
    blog_posts = Blog.objects.all().order_by("-published_at")
    return render(request, "django_project/homepage.html", {"blogs": blog_posts})


def about(request):
    return render(request, "django_project/about.html")


def article(request, pk):
    blog_post = Blog.objects.filter(pk=pk).first()
    if blog_post is None:
        return redirect("not_found")
    return render(request, "django_project/article.html", {"blog": blog_post})


@login_required
def blog_post(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")

    return render(request, "django_project/create-blog.html", {"form": form})


@login_required
def delete_blog(request, pk):
    post = Blog.objects.filter(pk=pk).first()
    if post is None:
        return redirect("not_found")
    if post.author != request.user:
        return HttpResponse("Permission Denied. You're not the owner of the blog post.", status=403)

    post.delete()
    return redirect("home")


@login_required
def my_blogs(request):
    blog_posts = Blog.objects.filter(author=request.user).order_by("-published_at")
    return render(request, "django_project/my_blogs.html", {"blogs": blog_posts})


@login_required
def edit_blog(request, pk):
    blog = Blog.objects.filter(pk=pk).first()
    if blog is None:
        return HttpResponse("Blog not found.", status=404)
    if blog.author != request.user:
        return HttpResponse("You are not authorized to edit this blog.", status=403)

    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("article", pk=blog.pk)

    return render(request, "django_project/edit-blog.html", {"form": form, "blog": blog})


def not_found(request, exception=None):
    return render(request, "django_project/404.html", status=404)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "registration/register.html", {"form": form})
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    user_posts = Blog.objects.filter(author=request.user).order_by("-published_at")
    return render(request, "registration/profile.html", {"blogs": user_posts})
