# user.views.recruter.py

"""
Vue du tableau de bord du recruteur
"""

from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

from dash import mixins
from job import models, forms
from message.models import Message
from user.models import CustomUser 
from user.forms import CompanyUpdateForm
from user.decorators import user_is_recruiter


class DashboardView(mixins.DispatchRecruiterMixin, generic.TemplateView):
    template_name = "dash/company/index.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        offers = models.Offer.objects.filter(
            user__id=self.request.user.id
        )
        candidates = models.Apply.objects.filter(
            offer__user_id=self.request.user.id
        )
        messages = Message.objects.filter(
            author=self.request.user.id
        )

        kwargs['offers'] = offers[:3]
        kwargs['offers_count'] = offers.count()

        kwargs['candidates'] = candidates[:3]
        kwargs['candidates_count'] = candidates.count()

        kwargs['messages'] = messages[:3]
        kwargs['messages_count'] = messages.count()

        kwargs['page_title'] = "dashboard"
        return super(DashboardView, self).get_context_data(**kwargs)


dashboard = DashboardView.as_view()


@login_required
def settings(request):
    user = request.user
    if request.method == "POST":
        form = CompanyUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Information entreprise mise a jour avec succes")
            return redirect("dashboard:recruiter_settings")
        else:
            messages.error(request, f"{form.errors}")
            return redirect("dashboard:recruiter_settings")
    else:
        form = CompanyUpdateForm(instance=user)

    template = "dash/company/settings.html"
    context = {"form": form, 'page_title': 'paramètre'}

    return render(request, template, context)


class OfferListView(mixins.CompanyMixin, generic.ListView):
    model = models.Offer
    paginate_by = 10
    context_object_name = "offers"
    template_name = "dash/company/list_offer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offers"] = models.Offer.objects.filter(
            user__id=self.request.user.id)
        return context


offer_list_view = OfferListView.as_view(
    extra_context={'page_title': "liste de vos offres d'emploi"}
)


class OfferCreateView(
    SuccessMessageMixin,
    mixins.CompanyMixin,
    generic.CreateView
):
    model = models.Offer
    form_class = forms.OfferPostFrom
    success_message = "Offer successfully created!"
    template_name = "dash/company/create_offer.html"
    extra_context = {'page_title': "publier une offre d'emploi"}


offer_create_view = OfferCreateView.as_view()


class OfferUpdateView(
    SuccessMessageMixin,
    mixins.CompanyMixin,
    generic.UpdateView
):
    model = models.Offer
    form_class = forms.OfferPostFrom
    success_message = "Offer successfully updated !"
    template_name = "dash/company/create_offer.html"
    extra_context = {'page_title': "mettre à jour l'offre d'emploi"}


offer_update_view = OfferUpdateView.as_view()


class OfferDeleteView(
    SuccessMessageMixin,
    mixins.CompanyMixin,
    generic.DeleteView
):
    model = models.Offer
    success_message = "Offer successfully deleted !"
    template_name = "dash/company/delete_offer.html"

    def get_success_url(self):
        return reverse('dashboard:recruiter_delete_offer')


offer_delete_view = OfferDeleteView.as_view()


class OfferCandidateApplyList(mixins.DispatchRecruiterMixin, generic.ListView):
    model = models.Apply
    paginate_by = 5
    context_object_name = "candidates"
    extra_context = {'page_title': "liste de vos candidats"}
    template_name = 'dash/company/offer_candidate_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            offer__user_id=self.request.user.id
        )


offer_candidate_list_view = OfferCandidateApplyList.as_view()


class OfferCandidateApplyDetail(mixins.DispatchRecruiterMixin, generic.DetailView):
    """
    Detail sur le profile du candidat
    """

    model = models.Apply
    paginate_by = 5
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "candidat"
    template_name = 'dash/company/offer_candidate_detail.html'


offer_candidate_detail_view = OfferCandidateApplyDetail.as_view()


class CandidateApplyPerOfferView(mixins.DispatchRecruiterMixin, generic.ListView):
    """
    List des candidats par offre
    """

    model = models.Apply
    paginate_by = 5
    template_name = 'dash/company/candidate_per_list.html'
    context_object_name = 'candidates'

    def get_queryset(self):
        return self.model.objects.filter(offer_id=self.kwargs['offer_id']).order_by('id')

    def get_context_data(self, **kwargs):
        kwargs['offers'] = self.objects.get(id=self.kwargs['offer_id'])
        return super().get_context_data(**kwargs)


candidate_per_offer =  CandidateApplyPerOfferView.as_view()
