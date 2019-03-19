from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def auth(request):
    errors_list = []
    user_loggedin = 'Guest'
    if request.method == 'POST':
        print('log in : ', request.POST.get('name'), request.POST.get('password'))
        name = request.POST.get('name')
        password = request.POST.get('password')
        usergo = authenticate(username=name, password=password)
        if usergo is not None:
            auth_login(request, usergo)
            user = User.objects.get(username=name)
            return HttpResponseRedirect("/success/")
    context = {'errors_list': errors_list, 'user_loggedin': user_loggedin}
    return render(request, 'login/auth.html', context)


def success(request):
    return render(request, 'login/success.html')
