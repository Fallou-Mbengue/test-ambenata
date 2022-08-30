from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views.generic import View, CreateView

from user.forms import AccountCreationForm
from user.models import CustomUser


class UserCreateView(CreateView, View):
    template_name = "user/register.html"
    form_class = AccountCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            account_type = form.cleaned_data.get("account_type")
            mail_to_lower = email.lower()
            if password1 == password2:
                if CustomUser.objects.filter(email=mail_to_lower).exists() or CustomUser.objects.filter(phone=phone).exists():
                    messages.error(
                        request, "Cet Email/Téléphone est déja utilisé")
                    return redirect("register")
                else:
                    user = CustomUser.objects.create_user(
                        email=mail_to_lower,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                    )
                    if account_type == "investor":
                        user.is_investor = True
                    elif account_type == "project_owner":
                        user.is_project_owner = True
                    elif account_type == "job_seeker":
                        user.is_job_seeker = True
                    elif account_type == "recrutor":
                        user.is_recruiter = True
                    user.save()
                    auth_user = authenticate(
                        request, email=mail_to_lower, password=password1
                    )
                    if auth_user is not None:
                        auth_login(request, auth_user)
                        return redirect("page:home")
            else:
                messages.error(
                    request, "Les mots de passe ne sont pas identiques")
                return redirect("register")
        return render(request, self.template_name, {"form": form})
