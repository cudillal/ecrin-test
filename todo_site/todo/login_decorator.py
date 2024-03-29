"""
Python decorator to show an alert message after attempting to load a page where being logged in is required while not logged in.
Source: https://stackoverflow.com/questions/2723842/django-message-framework-and-login-required
"""

from functools import wraps

from django.contrib import messages


default_message = "Please log in to see your to-do list."

def user_passes_test(test_func, message=default_message):
    """
    Decorator for views that checks that the user passes the given test,
    setting a message in case of no success. The test should be a callable
    that takes the user object and returns True if the user passes.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                messages.error(request, message)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def login_required_message(function=None, message=default_message):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        message=message,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator