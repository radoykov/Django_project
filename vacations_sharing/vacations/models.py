from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Vacation(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length= 2000, null=True)
    picture_url = models.URLField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    likes = models.ManyToManyField(User, related_name="likes")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.CharField(max_length=4000)
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.text
    