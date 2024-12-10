from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            new_user.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully!")

            login(request, new_user)
            return redirect("core:index")
        else:
            messages.error(request, "Please fix the errors in the form.")
    else:
        form = UserRegisterForm()

    return render(request, "userauths/sign-up.html", {"form": form})


def login_view(request):
    force_login = request.GET.get("force", False)
    if request.user.is_authenticated and not force_login:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("partials:base")
        else:
            messages.warning(request, "Invalid email or password.")

    return render(request, "userauths/log-in.html")

def logout_view(request):
    logout(request)
    messages.success(request," You have logged out")
    return redirect("userauths:sign-in")
