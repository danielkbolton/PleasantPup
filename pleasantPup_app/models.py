from django.db import models
from django.contrib.auth.models import User

# Create your models here.


""" ---------- START USER CLASSES ---------- """

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField(default="No content provided")
    image_link = models.TextField(default="No image provided")
    # image_upload = models.ImageField(upload_to='prof_images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

""" ---------- END USER CLASSES ---------- """






""" ---------- START DOG CLASSES ---------- """

class Breed(models.Model):
    breed = models.CharField(max_length=200)
    physical_characteristics = models.TextField(default=0)
    personality_temperament = models.TextField(default=0)
    care = models.TextField(default=0)
    health = models.TextField(default=0)
    history_background = models.TextField(default=0)
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.breed

class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog')
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
 
    def __str__(self):
        return self.name

class DogProfile(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='dog_profile')
    age = models.TextField(default=0)
    image = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.dog

""" ---------- END DOG CLASSES ---------- """

