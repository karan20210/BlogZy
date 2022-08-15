from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Blog(models.Model):
    
    class category_choices(models.TextChoices):
        TECHNOLOGY = 'Technology', ('Technology')
        SPORTS = 'Sports', ('Sports')
        LIFESTYLE = 'Lifestyle',('Lifestyle')
    
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices=category_choices.choices, default=category_choices.TECHNOLOGY)
    content = HTMLField()
    slug = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Blog: " + self.title + " by " + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Comment by " + str(self.user) + " on " + str(self.blog) + " at " + str(self.time)