from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    # The auto_now_add=True means the default created time is the time of post entry.
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # The - prefix on created_on indicates the posts are displayed in descending order of creation date.
        # If no leading - is used, then the order is ascending,
        # and if a ? prefix is used, then the order is randomised.
        ordering = ["-created_on"]

    def __str__(self):
        # We pass self into the __str__ method to provide access to the Model instance's attributes and data,
        # which allows us to customise the string representation of the instance.
        return f"The title of this post is {self.title}"


class Comment(models.Model):
    name = models.CharField(max_length=200,default="test")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



