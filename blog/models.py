from django.db import models
from markdownx.models import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()
    excerpt = models.TextField(blank=True, help_text="Resumen corto del post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
