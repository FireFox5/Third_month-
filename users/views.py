from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from users.forms import RegisterForms, LoginForms


def register_view(request):
    forms = RegisterForms
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["last_name"]
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]
        if password2 != password:
            return render(request, "register.html", context={'form': forms})
        if not username:
            return render(request, "register.html", context={'form': forms})
        user = User.objects.create_user(
            username=username, password=password, first_name=first_name,
            last_name=last_name, email=email
        )
        if user:
            login(request, user)
        return redirect('blogs')
    return render(request, "register.html", context={'form': forms})


def login_view(request):
    forms = LoginForms
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return redirect('blogs')
        else:
            return render(request, "login.html", context={'form': forms})
    if request.method == "GET":
        return render(request, "login.html", context={'form': forms})


def logout_view(request):
    logout(request)
    return redirect('blogs')