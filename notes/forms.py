#-*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, Textarea

from notes.models import Note


class NoteForm(ModelForm):
    """form for note model"""
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['name'].required = True
        self.fields['content'].label = ''
        self.fields['content'].required = True
        self.fields['public'].label = \
            'Сделать доступной для наших посетителей?'
        self.fields['on_top'].label = 'Держать всегда наверху?'

    class Meta:
        model = Note
        fields = ('name', 'content', 'public', 'on_top')
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название записки...',
                'class': 'input-xxlarge'}),
            'content': Textarea(attrs={
                'placeholder': 'Текст записки тут...',
                'class': 'input-xxlarge'}),
        }
