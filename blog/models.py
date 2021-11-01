from django.db import models
from django.contrib.auth.models import User
from django.http import request


class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
STATUS = [
    ('draft', 'Draft'),
    ('published', 'Published'),
   ]

class Post(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE )
    category = models.ForeignKey(Category , related_name='user', on_delete=models.CASCADE )
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='post', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10 , choices=STATUS)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.title
    
        
class Proflie(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_image = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.CharField(max_length=250)
    
    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    
    def __str__(self):
        return f'commentator {self.user} - post {self.post}'  

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title
    
               
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title



    
      
     