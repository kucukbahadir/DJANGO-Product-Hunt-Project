from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if  len(str(request.POST['password1']))>3 and request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request,'account/signup.html', {'error':'Username has already taken..\nPlease try another one!'})
            except User.DoesNotExist :
                user= User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'account/signup.html', {'error':'Passwords have to match !!'})


    else:
        return render(request,'account/signup.html')



def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html', {'error':'Username or Password is not correct !!'})
    else :
        return render(request,'account/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('home')