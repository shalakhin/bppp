#-*- coding: utf-8 -*-

from django import forms
from django.contrib.comments.forms import CommentForm


class CustomCommentForm(CommentForm):
    def __init__(self, *args, **kwargs):
        super(CustomCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ''
        self.fields['comment'].widget.attrs['class'] = 'input-xxlarge'
        self.fields['comment'].widget.attrs['placeholder'] = \
            'Текст комментария сюда вписывай...'
