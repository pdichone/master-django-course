from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": ""}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "I love this recipe!",
                    "rows": "3",
                }
            )
        }
