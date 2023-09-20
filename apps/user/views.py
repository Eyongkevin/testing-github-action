from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
def list_users(request):
    users = User.objects.all()

    context = {"users": users}
    return render(request, "user/list_users.html", context)


def list_users_old(request):
    users = User.objects.all()
    user_cnt = users.count()

    context = {"users": users, "user_cnt": user_cnt}
    return render(request, "user/list_users.html", context)


def login_view(request):
    # unbound state
    error_message = None
    form = AuthenticationForm()

    if request.method == "POST":
        # bound state
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Authenticate the user.

            user = authenticate(
                username=username,
                password=password,
            )
            if user is not None:
                # retain user's id in the session
                login(request, user)
                # we shall create the profile url/view and template
                return redirect("profile")

        else:
            error_message = "Sorry, something went wrong. Try again"

    context = {"form": form, "error_message": error_message}

    return render(request, "user/login.html", context)


@login_required
def profile(request):
    context = {"user": request.user}
    return render(request, "user/profile.html", context)
