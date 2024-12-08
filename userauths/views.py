from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save user with hashed password
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            new_user.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully!")

            # Login the user directly
            login(request, new_user)
            return redirect("core:index")
        else:
            messages.error(request, "Please fix the errors in the form.")
    else:
        form = UserRegisterForm()

    return render(request, "userauths/sign-up.html", {"form": form})


def login_view(request):
    return render(request, "userauths/log-in.html")
