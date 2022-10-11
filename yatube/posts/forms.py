from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {'text': 'Текст поста', 'group': 'Группа'}
        help_texts = {'group': 'Группа, к которой будет относиться пост',
                      'text': 'Текст нового поста'}
        fields = ["text", "group"]
