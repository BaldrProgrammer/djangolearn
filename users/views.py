from django.shortcuts import render

def email_verification(request):
    return render(request, 'users/email_verification.html')

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    return render(request, 'users/registration.html')

def profile(request):
    return render(request, 'users/profile.html')
