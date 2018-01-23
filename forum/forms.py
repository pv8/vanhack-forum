from django import forms

from .models import Comment, Post, Category


class PostForm(forms.ModelForm):
    detail = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), max_length=2000)

    class Meta:
        model = Post
        fields = ('subject', 'detail', 'categories', )


class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), max_length=1500)

    class Meta:
        model = Comment
        fields = ('message', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', )

    def clean_name(self):
        data = self.cleaned_data['name']
        return data.lower()