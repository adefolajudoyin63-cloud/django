from django.forms import ModelForm
from django_project.models import Blog


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ["headline", "body"]