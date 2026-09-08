from django import forms

from posts.models import Post

BANNED_WORDS = ("war", "ban", "BEGIN")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "image", "category", "tags")

    def clean_title(self):
        title = self.cleaned_data["title"]

        if title in BANNED_WORDS:
            raise forms.ValidationError("title has banned word!")

        return title
