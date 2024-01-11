
from django import forms
from .models import Movie, Genre
from community.models import Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)