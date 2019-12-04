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
    physical_characteristics = models.CharField(max_length=40000)
    personality_and_temperament = models.CharField(max_length=40000)
    breed_care = models.CharField(max_length=40000)
    health_info = models.CharField(max_length=40000)
    history_and_background = models.CharField(max_length=40000)
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.breed





class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog')
    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.name