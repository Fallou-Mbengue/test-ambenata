# dash.mixins.py

from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from user import decorators


class DispatchMixin:
    @method_decorator(login_required(login_url=reverse_lazy('register')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


class DispatchRecruiterMixin(DispatchMixin):
    @method_decorator(decorators.user_is_recruiter)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


class CompanyMixin(DispatchRecruiterMixin):

    def form_valid(self, form):
        offer = form.save(commit=False)
        offer.user = self.request.user
        form.instance.user = self.request.user
        offer.save()
        return super(CompanyMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:recruiter_list_offer')


class DispatchProjectOwnerMixin(DispatchMixin):
    @method_decorator(decorators.user_is_project_owner)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


class ProjectOwnerMixin(DispatchProjectOwnerMixin):

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user
        form.instance.user = self.request.user
        project.save()
        return super(ProjectOwnerMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:project_owner_list_project')
