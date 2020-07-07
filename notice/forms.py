from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '제목',
        })

    class Meta:
        model = Article
        fields = ('title', 'content', )
