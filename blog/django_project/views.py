from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
#Create your views here
#Display Hello World
=======
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217


# Create your views here.


def homepage(request):
    # Retrieve all the blog posts
    # from the database
    blog_posts = Blog.objects.all()

    return render(request, "django_project/homepage.html", {
        "blogs": blog_posts
    })


def article(request):
    return render(request, "django_project/article.html")

<<<<<<< HEAD
@login_required()
=======
@login_required
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
def blog_post(request):
    # Create an empty form
    form = BlogForm()

    # Handle form submission
    if request.method == "POST":
        # Put the submitted data into the form
        form = BlogForm(request.POST)
        if form.is_valid():# Check if the form is valid
            post = form.save(commit=False)
            post.author = request.user
            post.save()# Save the form data to the database
            return redirect("/")# Redirect to the homepage

    # Display the form
    return render(request, "django_project/create-blog.html", {
        "form": form
    })


# get the id 
# check the db to see if theres any blog post with the ID exist
# Conditionally check if it exists
    # Render the page with the blog post
# Else
    # Redirect the user to /not found

def article(request, pk):
    #scan  through the blog tables
    # and get the first blog_post whose its ID 
    # Is the same  as the primary key
    blog_posts = Blog.objects.filter(id=pk)  #use filters it doesn't raise error if page doesn't exist, gets goal is to retrieve a single objet unlike filter

    if  blog_posts.exists():
        return render(request, "django_project/article.html", {"blog": blog_posts.first()})
    else:
        return redirect("/not-found")


<<<<<<< HEAD
    
@login_required()
def delete_blog(request, pk):
    #this finds the post by its primary key or return error if not found
    post = Blog.objects.filter(pk=pk)
    if post is not None:
        if post.author != request.user:
            return HttpResponse("Permission Denied. You;re not the owner of the blog post.", status=403)
=======
@login_required
# view blogs belonging to logged in user
def my_blogs(request):
    blog_posts = Blog.objects.filter(author=request.user).order_by("-published_at")
    return render(request, "django_project/my_blogs.html", {"blog": blog_posts})


#if using reverse accessor
#user_posts = user.blog_set.all()


@login_required
def delete_blog(request, pk):
    #this finds the post by its primary key or return error if not found
    post = Blog.objects.filter(pk=pk).first()
    if not post:
        return redirect("/not-found")
    if post.author != request.user:
        return redirect("/not-found")
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
    #function to delete from the db
    post.delete()
    #redirect to home
    return redirect('home')

@login_required
def edit_blog(request, pk):
    # Find the blog post, or send the user to not-found
    blog = Blog.objects.filter(pk=pk).first()
    if not blog:
        return HttpResponse("Blog not found.")
    if blog.author != request.user:
        return HttpResponse("You are not authorized to edit this blog.")

    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "django_project/edit-blog.html", {
        "form": form,
        "blog": blog
    })

def not_found(request, exception=None):
    return render(request, "django_project/404.html", status=404)

<<<<<<< HEAD
# def not_found(request):
#     return HttpResponse("Not found")



@login_required()
def edit_blog(request, pk):
    #Retrieved all blog posta that shared/have the id
    # id=pk -> id: field
    # field() Returns Queryset
    blog_post = Blog.objects.filter(id=pk)



     #Checks if any blog posts were returned
    #if not, redirect the user to not_found

    if not blog_post.exists():
        return redirect("/not_found")

    blog_post = blog_post.first()
    if blog_post.author != request.user:
        return HttpResponse("Permission Denied. You're not the owner of the blog post.", status=403)



    

    blog_post = blog_post.first()

    form = BlogForm(instance=blog_post)

    #We check if user submit a form

    if request.method =="POST":
        form = BlogForm(request.POST, instance=blog_post)
        #Check if the form is valid i.e. user entered valid data
        if form.is_valid():
            _post = form.save(commit=False)
            _post.author = request.user
            _post.published_at = blog_post.published_at
            _post.save()
            form.save()

        


            # Return redirect(f"/article/{blog_post.pk}/")
            return redirect('read-blog', pk=blog_post.pk)
        #Display a template to the end-user
        return render(request, "daily_news/edit_blog.html", {"blog_post": blog_post})


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #usercreation form item - username, password, email,
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    user = request.user
    #use the reverse accesor to obtain all the posts that belong to the user
    #and assign it to the variable called 'user_posts'
    user_posts = user.blog_set.all()
    return render(request, "registration/profile.html", context={'blogs': user_posts})

=======


def login(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        error = "Username or password is incorrect."
    return render(request, "signup/login.html", {"error": error})


def register(request):
    error = None
    if request.method == "POST":
        password = request.POST.get("password1", "")
        confirm_password = request.POST.get("password2", "")
        if password != confirm_password:
            error = "Passwords do not match."
        else:
            form = UserCreationForm({
                "username": request.POST.get("username", ""),
                "password1": password,
                "password2": confirm_password,
            })
            if form.is_valid():
                user = form.save(commit=False)
                user.email = request.POST.get("email", "")
                user.save()
                auth_login(request, user)
                return redirect("home")
            error = " ".join(
                message
                for messages in form.errors.values()
                for message in messages
            )
    return render(request, "signup/signup.html", {"error": error})
>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
