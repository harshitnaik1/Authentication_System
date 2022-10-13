from datetime import datetime
from email.errors import MessageError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import Employee
from auth import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if Employee.objects.filter(username=username):
            messages.error(request, "Username Already Exist! Please try another username")
            return redirect('index')
        if Employee.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('index')
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        if pass1 != pass2:
            messages.error(request, "password did't matched")

        new_emp = Employee(username=username, first_name=first_name, last_name=last_name, email=email, pass1=pass1, pass2=pass2)
        new_emp.save()
        messages.success(request, "You have been added succesfully")

        subject = "Welcome to GFG-Django login!"
        message = "Hello" + Employee.first_name + "!! \n" + "Welcome to GFG!! \n Thank you for visiting our website"
        from_email = settings.EMAIL_HOST_USER
        to_list = [Employee.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)

        
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = Employee.first_name
            return render(request, 'index.html', {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('index')
    return render(request, 'signin.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged out succesfully!")
    return redirect('index')