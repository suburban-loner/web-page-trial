from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    """View function that renders the home page if the user is logged in, otherwise redirects to the login page.
    Parameters:
    ----------
    request : HttpRequest object
        The HTTP request object.
    Returns:
    -------
    HttpResponse object
        A rendered home template if the user is logged in, otherwise a redirect to the login page."""
    return render(request, 'home.html')

def batman(request):
    """View function that renders the batman page.
    Parameters:
    ----------
    request : HttpRequest object
        The HTTP request object.
    Returns:
    -------
    HttpResponse object
        A rendered batman template."""
    return render(request, 'batman.html')

def joker(request):
    """View function that renders the joker page.
    Parameters:
    ----------
    request : HttpRequest object
        The HTTP request object.
    Returns:
    -------
    HttpResponse object
        A rendered joker template."""
    return render(request, 'joker.html')

def heroes(request):
    """View function that renders the heroes page.
    Parameters:
    ----------
    request : HttpRequest object
        The HTTP request object.
    Returns:
    -------
    HttpResponse object
        A rendered heroes template."""
    return render(request, 'heroes.html')

def villains(request):
    """View function that renders the villains page.
    Parameters:
    ----------
    request : HttpRequest object
        The HTTP request object.
    Returns:
    -------
    HttpResponse object
        A rendered villains template."""
    return render(request, 'villains.html')
