from django import forms
from markdownx.widgets import MarkdownxWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content']
        widgets = {
            'content': MarkdownxWidget(),
        }