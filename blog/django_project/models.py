from django.db import models


class Blog(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.headline} by {self.author}"