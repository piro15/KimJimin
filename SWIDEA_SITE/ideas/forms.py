from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-radius: 10px;'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border-radius: 10px;',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'border-radius: 10px;'
            }),
            # 'interest': forms.NumberInput(attrs={
            #     'class': 'form-control',
            #     'style': 'border-radius: 10px; '
            #     'width: 65px;'})
        }
