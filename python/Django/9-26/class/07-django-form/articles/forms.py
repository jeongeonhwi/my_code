from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     # form필드에서는 CharField에서 맥스랜은 필수인자가 아니다.
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title'
            }
        )
    )
    # model 등록
    class Meta:
        model = Article
        # Article에서 받은 요소중 모든 요소를 입력받는다는 뜻
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)