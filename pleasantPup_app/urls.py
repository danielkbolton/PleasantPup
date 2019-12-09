from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('training/',views.training, name='training'),


    path('training/name/', views.name, name='name'),
    path('training/sit/', views.sit, name='sit'),
    path('training/sit/level2', views.sit2, name='sit2'),
    path('training/sit/level3', views.sit3, name='sit3'),
    path('training/down/', views.down, name='down'),
    path('training/stand/', views.stand, name='stand'),
    path('training/stay/', views.stay, name='stay'),
    path('training/settle/', views.settle, name='settle'),
    path('training/come/', views.come, name='come'),


    path('dog/new/', views.dog_create, name='dog_create'),
    path('dog/<int:dog_pk/', views.dog_profile, name='dog_profile'),
    path('dog/<int:dog_pk>/edit/', views.dog_edit, name='dog_edit'),
    path('dog/<int:dog_pk>/delete/',views.dog_delete, name='dog_delete'),
    path('dog/<int:dog_pk>/profile', views.dog_profile, name='dog_profile')
]