from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
            'author'  # нужно сделать автоматическое определение автора
        ]
