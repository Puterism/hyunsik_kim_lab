from django import forms
from .models import Profile, Menu, Item

import datetime


def get_now_year():
    return datetime.date.today().year


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '이름',
        })

        self.fields['position'].widget.attrs.update({
            'placeholder': '직위',
        })

        self.fields['location'].widget.attrs.update({
            'placeholder': '소속(위치)',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': '이메일',
        })

    class Meta:
        model = Profile
        fields = ('name', 'position', 'location', 'email', 'photo', )

    photo = forms.ImageField(
        label='',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'image-upload'
        })
    )


class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)

        self.fields['header'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '메뉴 이름',
        })

    class Meta:
        model = Menu
        fields = ('header', )


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        self.fields['menu'].widget.attrs.update({
            'autoFocus': 'autoFocus',
        })
        self.fields['year'].widget.attrs.update({
            'placeholder': '연도',
        })
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목 (필수 입력)',
        })
        self.fields['subtitle'].widget.attrs.update({
            'placeholder': '부제목',
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': '설명',
        })

        choices = [(m.id, m) for m in Menu.objects.all()]
        choices = [('', '------ 메뉴 선택 ------')] + choices[0:]
        self.fields['menu'].choices = choices

    class Meta:
        model = Item
        fields = ('menu', 'year', 'title', 'subtitle', 'description', )
