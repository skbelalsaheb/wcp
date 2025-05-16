from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from django.contrib.auth.models import User


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
            login(request, user)
            return redirect("/")
        return render(request, 'login.html', {'error': 'Invalid username or password'})


class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        login(request, user)
        return redirect('/')