from django import forms

from .models import Todo

INPUT_CLASSES = 'input'

class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'content', 'related_date',)

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'input title-input h3',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'Enter text',
                'class': 'input text',
            }),

            'related_date': forms.DateInput(attrs={
                'placeholder': 'yyyy-mm-dd',
                'class': 'input input-date text',
            }),
        }

class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'content', 'related_date',)

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'input title-input h3',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'Enter text',
                'class': 'input text',
            }),
            
            'related_date': forms.DateInput(attrs={
                'placeholder': 'yyyy-mm-dd',
                'class': 'input input-date text',
            }),
        }