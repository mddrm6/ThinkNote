from django import forms

from .models import Note

INPUT_CLASSES = 'input'

class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'input title-input h3',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'Enter text',
                'class': 'input text',
            }),
        }

class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content',)

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'input title-input h3',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'Enter text',
                'class': 'input text',
            }),
        }