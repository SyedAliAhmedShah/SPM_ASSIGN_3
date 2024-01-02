from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User

def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
def contact_view(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
def login_view(request):
    if request.method == 'POST':
        form = request.POST
        email = form.get('email')
        password = form.get('password')

        try:
            user = User.objects.get(user_email=email, password=password)
        except User.DoesNotExist:
            return render(request, 'login.html', {'form': form})
        else:
            return redirect('index')  # Redirect to the index page after login

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = request.POST
        email = form.get('email')
        password = form.get('password')

        user = User.objects.create(user_email=email, password=password)
        user.save()

        # Redirect to the login page after signup
        return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
