from django.shortcuts import render
from userauths.forms import UserRegisterForm

def register_view(request):

    if request.method == "POST":
        print("User registered successfully")

    else:
        print("User cannot be registered")
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request,"userauths/sign-up.html", context)
