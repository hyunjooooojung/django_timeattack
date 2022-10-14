from django.shortcuts import redirect, render
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        return redirect('/login')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            return render(request, 'user/login.html')
        
    
    elif request.method == "GET":
        # 로그인된 사용자가 요청하는 것인지 검사
        user = request.user.is_authenticated
        if user: 
            return redirect('/home')
        else: #로그인이 되어있지 않으면
            return render(request, 'user/login.html')