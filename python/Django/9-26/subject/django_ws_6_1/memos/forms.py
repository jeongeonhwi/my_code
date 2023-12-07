from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the memo',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the summary',
            }
        )
    )
    class Meta:
        model = Memo
        fields = '__all__'