from django.contrib import admin
from .models import Profile
from .models import Breed
from .models import Dog

# Register your models here.


admin.site.register(Profile)
admin.site.register(Breed)
admin.site.register(Dog)