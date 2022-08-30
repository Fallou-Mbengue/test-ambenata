# formulaire contact

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Formulaire contact
    """
    name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(
        {
            "class": "form-control",
        }
    ))
    email = forms.EmailField(label="Adresse email", widget=forms.EmailInput(
        {
            "class": "form-control smalls",
            "placeholder": "email@domain.com",
        }
    ))
    phone = forms.CharField(label="Numéro de téléphone", max_length=60, widget=forms.TextInput(
        {
            "class": "form-control form-tel",
            "placeholder": "763772260",
            "id": "phone",
            "type": "tel"
        }
    ))
    subject = forms.CharField(label="Sujet", max_length=100, widget=forms.TextInput(
        {
            "class": "form-control",
        }
    )
    )
    message = forms.CharField(label="Message", max_length=100, widget=forms.Textarea(
        {
            "class": "form-control",
            "cols": 30,
            "rows": 8,
        }
    ))

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message',
        ]
