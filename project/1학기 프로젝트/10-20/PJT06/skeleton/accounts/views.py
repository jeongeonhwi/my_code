from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인한 사용자가 들어오면 ???
    if request.user.is_authenticated:
        return redirect('boards:index')
    # method가 GET일때와 POST일 때
    if request.method == 'POST':
        # 회원가입을 진행하고 인덱스 페이지로 리다이렉트
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    elif request.method == 'GET':
        # 회원가입 페이지를 보여줘야함
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 사용자가 들어오면 ???
    if request.user.is_authenticated:
        return redirect('boards:index')
    # method가 GET일때와 POST일 때
    if request.method == 'POST':
        # 회원가입을 진행하고 인덱스 페이지로 리다이렉트
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    elif request.method == 'GET':
        # 회원가입 페이지를 보여줘야함
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


#섹션데이터를 요구하네
@require_POST
def logout(request):
    # 로그인 안된 사용자가 요청을 보내면 ?
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('boards:index')