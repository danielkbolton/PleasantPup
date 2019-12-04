from django.contrib import admin
from .models import Profile, Post
from .models import Breed, Dog, DogProfile


# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)

admin.site.register(Breed)
admin.site.register(Dog)
admin.site.register(DogProfile)