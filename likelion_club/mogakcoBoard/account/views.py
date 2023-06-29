from django.shortcuts import render, redirect 
from django.contrib import auth 
from django.contrib.auth.models import User 

# Create your views here.
def login(request):
    # POST 요청 시: 유저 확인 후 로그인  
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']
        # 데이터베이스에 있는 유저인지 확인
        user = auth.authenticate(request, username=userid, password=userpw)
        # 유저가 존재할 때 
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'login.html')
    # GET 요청 시: login 페이지 띄워주기 
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            return redirect('home')
    else:
        return render(request, 'signup.html')