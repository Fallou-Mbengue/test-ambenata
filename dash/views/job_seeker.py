from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from job.models import Offer

from user.forms import UpdateResumeForm, UserUpdateForm
from user.models import CustomUser


@login_required
def dashboard(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Information mise a jour avec succes")
            return redirect("dashboard:dashboard")
        else:
            messages.error(request, f"{form.errors}")
            return redirect("dashboard:dashboard")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "dash/job_seeker/index.html", {"form": form})


class OfferList(ListView):
    model = Offer
    context_object_name = "offers"
    template_name = "dash/job_seeker/list_offres.html"


class OfferDetail(DetailView):
    model = Offer
    template_name = "dash/job_seeker/detail_offre.html"


class CandidateUpdateView(UpdateView):
    model = CustomUser
    template_name = "candidate_edit.html"


class OfferApplyListView(ListView):
    model = Offer
    context_object_name = "offers"
    template_name = "dash/job_seeker/offres_postuler.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["offers"] = user.applied_job.all()
        return context


def user_resume(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("dashboard:view-resume")
    else:
        form = UpdateResumeForm(instance=user)
    return render(request, "dash/job_seeker/mon_cv.html", {'form': form})


class KpiView(TemplateView):
    template_name = "dash/job_seeker/kpi.html"
