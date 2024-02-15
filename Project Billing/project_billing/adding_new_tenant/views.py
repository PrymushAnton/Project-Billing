import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from .models import Contract

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
                user = authenticate(username = log, password = password)
                if user:
                    try:
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




def contract(request):
    context = {}
    
    if request.method == 'POST':
        building = request.POST.get('building')
        number_of_contract = request.POST.get('number_of_contract')
        date_beginning = request.POST.get('date_beginning')
        date_end = request.POST.get('date_end')
        date_of_agreement = request.POST.get('date_of_agreement')
        landlord = request.POST.get('landlord')
        tenant = request.POST.get('tenant')
        tenant_ps = request.POST.get('tenant_ps')
        type_of_contract = request.POST.get('type_of_contract')
        tax_for_ad = request.POST.get('tax_for_ad')
        in_work = request.POST.get('in_work')
        closed = request.POST.get('closed')
        comment = request.POST.get('comment')
        number_of_agreement = request.POST.get('number_of_agreement')
        main_agreement = request.POST.get('main_agreement')
        lot = request.POST.get('lot')
        print(type_of_contract)
        if building and number_of_contract and date_beginning and date_end and date_of_agreement and landlord and tenant and type_of_contract and number_of_agreement and main_agreement and lot:
            Contract.objects.create(
                building=building, 
                number_of_contract=number_of_contract, 
                date_beginning=date_beginning,
                date_end=date_end,
                date_of_agreement=date_of_agreement,
                landlord = landlord,
                tenant = tenant,
                tenant_ps = tenant_ps,
                type_of_contract = type_of_contract,
                tax_for_ad = tax_for_ad,
                in_work = in_work,
                closed=closed,
                comment=comment,
                number_of_agreement=number_of_agreement,
                main_agreement=main_agreement,
                lot=lot
            )
            
        else:
            context['error'] = 'Не всі поля заповнені!'

        
    return render(request, 'adding_new_tenant/contract.html', context)