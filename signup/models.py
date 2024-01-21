from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, default='Unknown')
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    author_id = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)  
    number_of_pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers', blank=True, null=True)
    book_id = models.CharField(max_length=10, unique=True, blank=True, null=True)   
