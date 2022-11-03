from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        label = {'text': 'Текст записи', 'group': 'Группа'}
        help_text = {'text': 'Введите текст записи',
                     'group': 'Выберите группу'
                     }
