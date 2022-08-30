# user.decorator.py

from django.core.exceptions import PermissionDenied


def user_is_investor(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_investor:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_is_project_owner(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_project_owner:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_is_job_seeker(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_job_seeker:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def user_is_recruiter(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_recruiter:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
