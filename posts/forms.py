# C:\blog_django\src\posts\forms.py

from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # Inclure 'is_restricted' dans les champs modifiables
        fields = ['title', 'content', 'status', 'is_restricted']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
        }

