from django import forms

from .models import Home, Site


class HomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': '메인 제목',
        })

        self.fields['subtitle'].widget.attrs.update({
            'placeholder': '메인 부제목',
        })

        self.fields['content'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '소개',
        })

    class Meta:
        model = Home
        fields = ('title', 'subtitle', 'content', )


class SiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': '사이트 제목',
        })

        self.fields['page_subtitle'].widget.attrs.update({
            'placeholder': '각 페이지 부제',
        })

        self.fields['address'].widget.attrs.update({
            'placeholder': '연구실 주소',
        })

        self.fields['tel'].widget.attrs.update({
            'placeholder': '연락 가능한 전화',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': '연락 가능한 이메일',
        })

    class Meta:
        model = Site
        fields = ('title', 'page_subtitle', 'address', 'tel', 'email', )

