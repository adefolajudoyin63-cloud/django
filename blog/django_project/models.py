from django.db import models

<<<<<<< HEAD
=======


>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
# Create your models here.
class Blog(models.Model):
    headline = models.CharField()
    body = models.TextField()
<<<<<<< HEAD
    author = models.ForeignKey('auth.User',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True
                              )
=======
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # author_email = models.EmailField(
    #     null=True, # Makes a column optional database specific feature
    #     default="any_author@email.com", #The fixed data that is used when the inpu is not provided
    #     blank=False,#Form-specific
    #     unique=True, # Users cant have same email
    #     max_length=30, #this indicates the maximum amount of chars that must be entered
    #     # choices=(
    #     #     ("test@email.com", "Author Test Email")#first part is whats is saved to the db, other part is whats is  displayed to the user
    #     # ), #this choices could be tuple, list and dictionaries we want to be able to restric the input to a number of email that could be able to be entered into the field
    #     primary_key=True, #Settin this here automatically makes our email the primary key value, any primary key we must be used must be value thats unique

>>>>>>> e3eaeebe311e669b2f75d19251302ed3ddb1d217
    published_at = models.DateTimeField(auto_now=True)



    def __str__(self):  #This helps us reference in dashboard with the headline of each blog
        return f"{self.headline} by {self.author}"
    