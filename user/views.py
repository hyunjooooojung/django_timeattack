from django.shortcuts import redirect, render
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    
    elif request.method == "POST":
        user = User()
        
        user.username = request.POST.get('username', '')
        # user.password = request.POST.get('password', ''), 
        #패스워드느 set_password로 설정해야한다!!
        user.set_password(request.POST.get('password', ''))
        user.phone = request.POST.get('phone', '')
        user.address = request.POST.get('address', '')
        user.save()
        
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
            return render(request, 'login.html')
        
    
    elif request.method == "GET":
        # 로그인된 사용자가 요청하는 것인지 검사
        user = request.user.is_authenticated
        if user: 
            return redirect('/home')
        else: #로그인이 되어있지 않으면
            return render(request, 'login.html')
        
        
def home(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return redirect('/login/')
        
        return render(request, 'home.html')