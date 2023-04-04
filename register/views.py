from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm

# Create your views here.
def register(response):
    """View function that handles registration form submissions.
    Parameters:
    ----------
    response : HttpResponse object
        The HTTP response object containing the registration form.
    Returns:
    -------
    HttpResponse object
        A redirect to the login page if the registration form is submitted and valid,
        or a rendered registration form if the form is not submitted or invalid.    """
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def login_request(request):
    """A view function that handles the login request.
    Parameters:
    ----------
    request : HttpRequest object
    The HTTP request object containing the form data.

    Returns:
    -------
    HttpResponse object
    A redirect to the IndexView if the login is successful, 
    or a rendered login template with the login form if the form is invalid or not submitted."""
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('website:IndexView')
    else:
        form = LoginForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
