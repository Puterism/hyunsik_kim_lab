from django import forms
from .models import Research

import datetime


def get_now_year():
    return datetime.date.today().year


class ResearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': '제목',
        })

        self.fields['author'].widget.attrs.update({
            'placeholder': '저자 (선택 입력)',
        })

    class Meta:
        model = Research
        fields = ('year', 'title', 'author', 'content',)

    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': '연도', 'autoFocus': 'autoFocus'}),
        initial=get_now_year,
        min_value=1970, max_value=get_now_year() + 10,
    )