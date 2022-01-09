from django.shortcuts import render
from django.shortcuts import redirect #did this for redirecting to another page
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features}) 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['con-pass']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Someone has taken this email')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect("register")
    else:
        return render(request, 'register.html')

def counter(request):
    comment = request.POST['comment']
    count = len(comment.split())
    return render(request, 'counter.html', {'count': count}) 