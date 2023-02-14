from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter a comment"}
        ),
    )
    class Meta:
        model = Comment
        fields = ['content']