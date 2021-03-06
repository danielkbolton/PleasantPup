from django import forms
#from django.forms.widgets import DateTimeInput

from . models import Profile, Dog, Breed, Post, Comment


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name','age','breed','image_link')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col'}),
            'age': forms.TextInput(attrs={'class': 'form-control col'}),
            'image_link': forms.TextInput(attrs={'class': 'form-control col'})
        }




class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)
        widgets = {
            'image_link': forms.TextInput(attrs={'class': 'form-control col'})
        }



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','content','image_link')



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)