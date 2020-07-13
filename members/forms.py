from django import forms

from .models import Member, Position


class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '이름',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': '이메일 (선택 입력)',
        })

    def resize(self, data, width, height, force=True):
        from io import BytesIO
        from PIL import Image as pil

        max_width = width
        max_height = height

        input_file = BytesIO(data.read())
        img = pil.open(input_file)

        if not force:
            img.thumbnail((max_width, max_height), pil.ANTIALIAS)
        else:
            src_width, src_height = img.size
            src_ratio = float(src_width) / float(src_height)
            dst_width, dst_height = max_width, max_height
            dst_ratio = float(dst_width) / float(dst_height)

            if dst_ratio < src_ratio:
                crop_height = src_height
                crop_width = crop_height * dst_ratio
                x_offset = int(src_width - crop_width) // 2
                y_offset = 0
            else:
                crop_width = src_width
                crop_height = crop_width / dst_ratio
                x_offset = 0
                y_offset = int(src_height - crop_height) // 3
            img = img.crop((x_offset, y_offset, x_offset + int(crop_width), y_offset + int(crop_height)))
            img = img.resize((dst_width, dst_height), pil.ANTIALIAS)

        image_file = BytesIO()
        img.save(image_file, 'JPEG')
        data.file = image_file
        return data

    def save(self, commit=True, *args, **kwargs):
        instance = super(MemberForm, self).save(commit=False)

        if instance.photo:
            instance.photo = self.resize(self.cleaned_data.get('photo'), 600, 600, force=True)
        if commit:
            instance.save()

        return instance

    class Meta:
        model = Member
        fields = ('photo', 'name', 'position', 'email', 'description',)

    photo = forms.ImageField(
        label='',
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'image-upload'
        })
    )

    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': '설명 (선택 입력)'
        })
    )


class PositionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '분류 입력...',
        })

    class Meta:
        model = Position
        fields = ('title',)
