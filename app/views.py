from django.shortcuts import render
from .models import *
from random import randint

# Create your views here.

def Register(request):
     return render(request, "app/Home.html")

def AddUser(request):
    try:
        firstname =request.POST['firstname']
        lastname = request.POST['lastname']
        birthday = request.POST['birthday']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        reapeatpassword = request.POST['reapeatpassword']
        user = User.objects.filter(email=email)
        if user:
                print("--------------2---------------")
                message = 'This email already exists'
                return render(request,("app/Home.html"), {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------3---------------")
                employeeid = randint(100000,9999999)
                newuser = User.objects.create(
                    email=email, password=password,employeeid=employeeid)
                newcust = customer.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,birthday=birthday ,phone=phone)
                return render(request,("app/Login.html"))
            else:
                print("--------------4---------------")
                message = "Password and confirm password doesn't match"
                return render(request,("app/Home.html"),{'message': message})
    except Exception as e1 :
        print("the error is--->",e1)

def Loginuser(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    print(user)
    if user:
        print("---enter-----")
        if user[0].password == password:
            return render(request,("app/User.html"))
        else:
            message = "Your password is incorrect or user doesn't exist"
            return render(request, ("app/Login.html"), {'message': message})
    else:
        message = "user doesn't exist"
        return render(request, ("app/Login.html"), {'message': message})     

