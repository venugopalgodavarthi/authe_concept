from django.shortcuts import render
from authe.forms import user_form, login_form
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register_view(request):
    form = user_form()
    if request.method == 'POST':
        print(request.POST)
        form = user_form(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Register process is success")
    return render(request=request, template_name='register.html', context={"form": form})


def login_view(request):
    form = login_form()
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        login(request, user)  # session creation
        return HttpResponse("login is success")
    return render(request=request, template_name='login.html', context={"form": form})


def logout_view(request):
    logout(request)  # session destroy
    return HttpResponse("logout is success")
