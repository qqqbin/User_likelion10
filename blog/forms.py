from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '제목'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '내용',
                'rows': '5'
                }),
        }