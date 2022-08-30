from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from user.models import CustomUser


class CandiateList(View):
    template_name = "user/candidate_list.html"

    def get(self, request, **kwargs):
        candidates = CustomUser.objects.candidates()
        return render(request, self.template_name, {"candidates": candidates})


class CandiateDetail(DetailView):
    model = CustomUser
    template_name = "user/candidate_detail.html"
    context_object_name = "candidate"
