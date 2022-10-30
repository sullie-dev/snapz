from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import random
import string


def idGenerator():
    upper_string = string.ascii_uppercase
    lower_string = string.ascii_lowercase
    numerical = string.digits

    alphabet = upper_string + lower_string + numerical
    random_character = random.sample(alphabet, 10)
    slug = "".join(random_character)
    return slug

# Create your models here.

randString = idGenerator()

class Post(models.Model):
    slug = models.SlugField(max_length=200, default=randString, unique=True)
    post_id = models.CharField(max_length=30, default=randString, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.post_id

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_text} - {self.name}"
    
    def number_of_comments(self):
        return self.comments.count()
    