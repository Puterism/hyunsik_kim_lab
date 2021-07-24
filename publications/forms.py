from django import forms

from .models import Description, Publication


class PublicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)

        self.fields['label'].widget.attrs.update({
            'autoFocus': 'autoFocus',
            'placeholder': '라벨 (선택 입력)',
        })

    class Meta:
        model = Publication
        fields = ('label', 'content', )

class DescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Description
        fields = ('description', )
