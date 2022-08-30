from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from user.models import CustomUser
from .models import Apply, Offer


class OfferList(ListView):
    model = Offer
    context_object_name = "jobs"
    template_name = "job/job_list.html"


class OfferDetail(DetailView):
    model = Offer
    template_name = "job/job_detail.html"
    context_object_name = "offer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class OfferCreateView(CreateView):
    model = Offer
    template_name = "job/job_create.html"
    success_url = "/jobs/"


class OfferUpdateView(UpdateView):
    model = Offer
    template_name = "Job/job_create.html"
    success_url = "/jobs/"


def new_apply(request, job_seeker_id, offer_id):
    job_seeker = get_object_or_404(CustomUser, pk=int(job_seeker_id))
    offer = get_object_or_404(Offer, pk=int(offer_id))
    apply = Apply.objects.filter(
        offer__id=offer.id, candidate__id=job_seeker.id)
    if apply.exists():
        messages.error(request, "Vous aviez deja postulé pour cette offre")
        return redirect("job:job-detail", slug=offer.slug)
    else:
        Apply.objects.create(offer=offer, candidate=job_seeker)
        # rediriger l'utilisateur vers les offres qu'il a postulés
        messages.success(request, "Vous avez postule avec succes")
        return redirect("dashboard:job_seeker_offres_postuler")
