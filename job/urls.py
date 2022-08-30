# job.urls.py

from os import name
from django.urls import path

from job.views import (OfferCreateView, OfferDetail, OfferList, OfferUpdateView, new_apply)

app_name = "job"

urlpatterns = [
    path("", OfferList.as_view(), name="job-list"),
    path("<slug:slug>/details/", OfferDetail.as_view(), name="job-detail"),
    path("create-job/", OfferCreateView.as_view(), name="job-create"),
    path("<slug:slug>/edit", OfferUpdateView.as_view(), name="job-edit"),
    path("apply/<int:job_seeker_id>/<int:offer_id>/", new_apply, name="new-apply")
]
