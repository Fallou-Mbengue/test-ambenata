from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect


def dashboard_view(request):
    user = request.user
    if user.is_authenticated:
        if user.is_staff:
            return redirect("dashboard:staff")
        if user.is_investor:
            return redirect("dashboard:investor_dashboard")
        if user.is_project_owner:
            return redirect("dashboard:project_owner_dashboard")
        if user.is_job_seeker:
            return redirect("dashboard:job_seeker_dashboard")
        if user.is_recruiter and user.is_staff:
            return redirect("dashboard:staff")
        if user.is_recruiter and not user.is_staff:
            return redirect("dashboard:recruiter_dashboard")
        else:
            return HttpResponseForbidden()
    return redirect("account_login")
