from django.shortcuts import redirect, render, HttpResponse
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # You may want to add additional checks here, like password confirmation
        if pass1 == pass2:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been created successfully")
            # return redirect('signin')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
    else:
        return render(request, 'home/signup.html')

def signin(request):
    return render(request, 'home/signin.html')

def signout(request):
    pass
