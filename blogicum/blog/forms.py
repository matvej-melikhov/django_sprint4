from django import forms
from django.contrib.auth import get_user_model

from .models import Post, Comment


User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={'type': 'date'},
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
