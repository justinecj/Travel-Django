from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        first_name1 = request.POST['first_name']
        last_name1 = request.POST['last_name']
        email1 = request.POST['email']
        password1 = request.POST['pass']
        cpassword1 = request.POST['cpass']

        if password1 == cpassword1:
            if User.objects.filter(username=username1).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request, "Email Already Exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username1, password=password1, first_name=first_name1, last_name=last_name1, email=email1)
                user.save()
                print("user created")
                messages.info(request, "user created")
                return redirect('login')
        else:
            print("password not same")
            messages.info(request,"password not same")
            return redirect('register')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
