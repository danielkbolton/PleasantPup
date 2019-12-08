from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('dog/new/', views.dog_create, name='dog_create'),
    path('dog/<int:dog_pk/', views.dog_profile, name='dog_profile'),
    path('dog/<int:dog_pk>/edit/', views.dog_edit, name='dog_edit'),
    path('dog/<int:dog_pk>/delete/',views.dog_delete, name='dog_delete'),
    path('dog/<int:dog_pk>/profile', views.dog_profile, name='dog_profile')
]