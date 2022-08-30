# ambenatna.urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Ambenatna"
admin.site.site_title = "Ambenatna"
admin.site.index_title = "Welcome to Ambenatna dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("user.urls")),
    path("", include("page.urls", namespace="page")),
    path("jobs/", include("job.urls", namespace="job")),
    path("projects/", include("project.urls", namespace="project")),
    path("dashboard/", include("dash.urls", namespace="dashboard")),
    path("accounts/", include("allauth.urls")),
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("summernote/", include("django_summernote.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
