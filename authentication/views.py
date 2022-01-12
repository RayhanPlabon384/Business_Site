from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def authlogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in successfully!!!')
            return redirect('about')
        else:
            messages.error(request, 'Invalid Username or Password!!!')
    return render(request,'authentication/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logged Out successfully!!!')
    return redirect('login')

def registration(request):
    if request.method =='POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!!!')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!!!')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request, 'Registration Successful!!')
                return redirect('login')

        else:
            messages.error(request, 'Passwords arenot matched!!!')

    return render(request,'authentication/registration.html')

def forgetpassword(request):
    return render(request,'authentication/forget.html')
