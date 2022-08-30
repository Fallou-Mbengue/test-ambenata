# message.forms.py

from django import forms

from message.models import Message
from django_summernote.widgets import SummernoteWidget


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}

        widgets = {
            'message': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control shadow-none'
