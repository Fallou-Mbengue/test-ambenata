# project.forms.py

from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Project, Category


class ProjectPostForm(forms.ModelForm):

    """
    Formulaire d'enregistrement projet
    """

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Catégorie de votre projet",
        empty_label=None,
        widget=forms.Select({"class": "form-control float-none"}))
    title = forms.CharField(
        label="Titre Projet", max_length=100,
        widget=forms.TextInput
    )
    budget = forms.DecimalField(
        label="Budget",
        widget=forms.TextInput)
    resume = forms.CharField(
        label="Résumer de votre projet",
        max_length=100,
        widget=forms.Textarea({"class": "form-control"}))
    description = forms.CharField(widget=SummernoteWidget(
        attrs={'width': '20%', 'height': '500px'}),)

    logo = forms.ImageField(
        label="Le Logo de votre projet")
    document = forms.FileField(
        label="Document de présentation(PitchDeck)")

    class Meta:
        model = Project
        fields = [
            'title', 'category', 'budget',
            'resume', 'description',
            'logo', 'document',
        ]

    # def __init__(self, *args, **kwargs):
       #  super(ProjectPostForm, self).__init__(*args, **kwargs)
        # for field in self.fields:
        # self.fields[field].widget.attrs.update({'class': 'form-control'})
        # self.fields['budget'].widget.attrs.update(
        #    {'class': 'form-control float-none'})
        # self.fields['resume'].widget.attrs.update(
        #    {'class': 'form-control float-none'})
        # self.fields['is_published'].widget.attrs.update(
        #   {'class': 'form-check-input shadown-none'})
