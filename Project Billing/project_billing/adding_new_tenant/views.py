import json

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def adding_new_tenant(request):
    context = {}
    
    if request.method == 'POST':
        if request.POST.get('register_id'):
            log = request.POST.get('login')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            email = request.POST.get('email')
            try:
                User.objects.create(username=log, password=password, first_name=first_name, last_name=last_name, email=email,)
            except IntegrityError:
                context['error'] = 'Користувач з такими даними вже існує!'
        if request.POST.get('log_id'):
            log = request.POST.get('login_log')
            password = request.POST.get('password_log')
            email = request.POST.get('email_log')
            user = User.objects.get(username=log, password=password, email=email)
            login(request, user)
            return redirect('main')
                       
                    
    return render(request, 'adding_new_tenant/adding_new_tenant.html')

def main(request):
    context = {}
    return render(request, 'adding_new_tenant/main.html', context)

def logouts(request):
    context = {}
    logout(request)
    return redirect('reg')