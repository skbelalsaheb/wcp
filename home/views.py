from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'contact.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Your account is pending admin approval.")
            else:
                messages.error(request, "Invalid credentials.")

            return render(request, "login.html")

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful. Await admin approval.")
            return redirect('login')
        return render(request, 'register.html')