from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    score = forms.FloatField(widget=forms.NumberInput(attrs={'step':0.5,'min':0,'max':5,}))
    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ('user_id',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('user_id', 'movie_id',)


