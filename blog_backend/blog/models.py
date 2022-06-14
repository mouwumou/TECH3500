from django.db import models
from django.contrib.auth.models import User


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="blog_img", null=True)
    content = models.CharField(max_length=1000)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta():
        ordering = ['-created_time']
        verbose_name = 'Blog'
        verbose_name_plural = verbose_name