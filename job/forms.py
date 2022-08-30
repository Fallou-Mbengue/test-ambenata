# job.forms.py

from django import forms
from job.models import Category, Offer
from django_summernote.widgets import SummernoteWidget


class OfferPostFrom(forms.ModelForm):

    """
    formulaire d'enregistrement d'emploi
    """

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Catégorie d'emploi",
        empty_label=None,
        widget=forms.Select({"class": "form-control float-none"}))

    class Meta:
        model = Offer
        fields = [
            'category', 'offer_type',
            'education_level',

            'title', 'content', 
            'document_desc', 
            
            'date_validation',
            'is_published',
        ]

        widgets = {
            'date_validation': forms.DateInput(attrs={'type': 'date'}, format='%d/%m/%Y'),
            'content': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(OfferPostFrom, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['offer_type'].widget.attrs.update(
                {'class': 'form-control float-none'})
            self.fields['education_level'].widget.attrs.update(
                {'class': 'form-control float-none'})
            self.fields['is_published'].widget.attrs.update(
                {'class': 'form-check-input shadown-none'})
