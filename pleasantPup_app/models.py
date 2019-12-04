from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.user.username





class Breed(models.Model):
    breed = models.CharField(max_length=200)
    physical_characteristics = models.TextField(default=0)
    personality_temperament = models.TextField(default=0)
    care = models.TextField(default=0)
    health = models.TextField(default=0)
    history_background = models.TextField(default=0)
    image_link = models.TextField(default=0)
    # image_upload = models.ImageField(upload_to='prof_images/')


    def __str__(self):
        return self.breed





class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog')
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
    image = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.name