from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



def reg(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password_1']
            confirm_password = request.POST['password_2']
            if password1 == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username already exists")
                    return redirect('reg')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email already exists")
                    return redirect('reg')
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return redirect('/')
            else:
               messages.info(request,"password and confirm password don't match")
    except:
        return redirect("home")
    return render(request,"registration.html")
