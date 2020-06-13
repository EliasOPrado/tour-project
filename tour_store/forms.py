from .models import Comment, Contact
from django import forms

#https://djangocentral.com/creating-comments-system-with-django/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject','message')

        #add styling to the form
        #for class attr you can use bootstrap or your own
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'subject':forms.TextInput(attrs={'class': 'form-control'}),
            'message':forms.Textarea(attrs={'class': 'form-control','height': '5rem'}),
        }
