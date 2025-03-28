from django import forms
from .models import Comment
from django import forms
from .models import Post
from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Ensure tags are displayed properly
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content
