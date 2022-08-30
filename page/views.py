from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render

from job.models import Offer
from page.forms import ContactForm
from project.models import Project


def home(request):
    jobs = Offer.objects.all()
    projects = Project.objects.all()
    return render(request, "index.html", {"jobs": jobs, "projects": projects})


def about(request):
    return render(request, "view/about.html")


def contacts(request):
    form = ContactForm(
        request.POST,
        request.FILES,
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Message enregistrer avec succes")
            return redirect("page:home")
    return render(request, "view/contact.html", {"form": form})
