# user.urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import candidate, shared

urlpatterns = [
    path("registration/", shared.UserCreateView.as_view(), name="register"),
    path("candidates/", candidate.CandiateList.as_view(), name="candidates"),
    path("candidates/<slug:slug>/", candidate.CandiateDetail.as_view(), name="candidate-details"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="change-password.html"),name="password_change",),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="change-password-done.html"), name="password_change_done",),
    
    # reset password
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="user/reset-password.html"),name="password_reset",),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="user/reset-password-done.html"), name="password_reset_done",),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="user/reset-password-confirm.html"), name="password_reset_confirm",),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="user/reset-password-complete.html"), name="password_reset_complete",),
]
