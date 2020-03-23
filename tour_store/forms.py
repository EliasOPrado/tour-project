from .models import Comment
from django import forms

#https://djangocentral.com/creating-comments-system-with-django/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')
