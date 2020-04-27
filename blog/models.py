from django.db import models
from django.contrib.auth.models import User
import django.db.models.deletion
from django.conf import settings
from tinymce.models import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    #image = models.ImageField(default=0, max_length=300, upload_to='images/')
    content = HTMLField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title