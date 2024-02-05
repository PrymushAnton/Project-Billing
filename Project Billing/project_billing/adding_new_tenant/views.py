import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render


# Create your views here.
def adding_new_tenant(request):
    context = {}
    if request.method == 'POST':
        setting = request.POST.get('setting')
        log = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if setting == 'registr':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            if log and first_name and last_name and password and email:
                try:
                    User.objects.create_user(username=log, password=password, first_name=first_name, last_name=last_name, email=email,)
                except IntegrityError:
                    context['error'] = 'Користувач з такими даними вже існує!'
                finally:
                    context['error'] = 'Акаунт зареєстровано!'
            else:
                context['error'] = "Не всі поля заповнено!"
        if setting == 'login':
            if log and password and email:
                if authenticate(username = log, password = password):
                    try:
                        user = User.objects.get(username=log, password=password, email=email)
                        login(request, user)
                    except:
                        context['error'] = 'Вибачте! Сталася невідома помилка...'
                    finally:
                        context['error'] = 'succ'
                else:
                    context['error'] = "Користувача не найдено!"
            else:
                context['error'] = "Не всі поля заповнено!"
        return JsonResponse(context)
    else:
        return render(request, 'adding_new_tenant/adding_new_tenant.html')

def logouts(request):
    context = {}
    logout(request)
    return redirect('reg')