# accounts.forms.py

from django import forms
from django.core.exceptions import ValidationError


from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,

)

from allauth.account.forms import SignupForm

from django_summernote.widgets import SummernoteWidget


from user.models import CustomUser


class UserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name",)


class UserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {
            "duplicate_email": "Cette adresse est déjà utilisé par un autre utilisateur."
        }
    )

    class Meta:
        model = CustomUser
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise ValidationError(self.error_messages["duplicate_email"])


class UserSignupForm(SignupForm):

    last_name = forms.CharField(label="prénom", max_length=100)
    first_name = forms.CharField(label="nom de famille", max_length=100)
    email = forms.EmailField(label="adresse email", required=False)
    is_investor = forms.BooleanField(
        label="je suis un investisseur",
        required=False
    )
    is_project_owner = forms.BooleanField(
        label="je suis un porteur de projet",
        required=False
    )
    is_job_seeker = forms.BooleanField(
        label="je cherche un emploi",
        required=False
    )
    is_recruiter = forms.BooleanField(
        label="je suis une entreprise",
        required=False
    )
    privacy = forms.BooleanField(required=True)

    def custom_signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.is_investor = self.cleaned_data['is_investor']
        user.is_job_seeker = self.cleaned_data['is_job_seeker']
        user.is_recruiter = self.cleaned_data['is_recruiter']
        user.is_project_owner = self.cleaned_data['is_project_owner']

        user.save()


ACCOUNT_TYPE_CHOICES = (
    ("investor", "Je suis investisseur"),
    ("project_owner", "je suis porteur de projet", ),
    ("job_seeker", "je suis chercheur d'emploi"),
    ("recrutor", "Je suis recruteur"),
)


class AccountCreationForm(forms.Form):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, label="Vous etes?", widget=forms.Select(
        {
            "class": "form-control my-2 float-none",
            "placeholder": "Votre profil",
        }
    ))
    first_name = forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(
        {
            "class": "form-control",
            "placeholder": "Doe",
        }
    ))
    last_name = forms.CharField(label="Nom de famille", max_length=100, widget=forms.TextInput(
        {
            "class": "form-control",
            "placeholder": "John",
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
    email = forms.EmailField(label="Adresse email", widget=forms.EmailInput(
        {
            "class": "form-control",
            "placeholder": "email@domain.com",
        }
    ))

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            {
                "class": "form-control",
                "placeholder": "Mot de passe",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirmation Mot de passe",
        widget=forms.PasswordInput(
            {
                "class": "form-control",
                "placeholder": "Confirmation Mot de passe",
            }
        ),
    )


class UserUpdateForm(forms.ModelForm):
    EXPERIENCE_CHOICES = (
        ("-1", "Moins d'une année"),
        ("1-3", "1-3 ans"),
        ("3-5", "3-5 ans"),
        ("5-10", "5-10 ans"),
        ("+10", "Plus de 10 ans"),
    )
    required_css_class = 'required'
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES, label="Experience", widget=forms.Select({
        'class': 'form-control float-none'}))

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'title',
            'email',
            'phone',
            'address',
            'experience',
            'avatar',
        ]


class CompanyUpdateForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'avatar',
            'description',
        ]

        widgets = {
            'description': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(CompanyUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            {
                "class": "form-control",
                "placeholder": "Mot de passe",
            }
        ),
    )
    password2 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            {
                "class": "form-control",
                "placeholder": "Mot de passe",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("email", "password1")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "avatar")


class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("resume",)
