from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Post title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "rows": 6,
                    "placeholder": "Write your content here...",
                }
            ),
        }
