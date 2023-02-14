from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    title = forms.CharField(
        label="Post Title",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Post Title"}
        ),
    )
    content = forms.CharField(
        label="Post Title",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Post Content"}
        ),
    )

    class Meta:
        model = Post
        fields = ['title', 'content']

