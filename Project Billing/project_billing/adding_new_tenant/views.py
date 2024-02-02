from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render


# Create your views here.
def adding_new_tenant(request):
    context = {}
    
    if request.method == 'POST':
        login = request.POST.get('login')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if request.method == 'POST':
            if login and first_name and last_name and password and email:
                try:
                    User.objects.create(username=login, email=email, password=password, first_name=first_name, last_name=last_name)
                except IntegrityError:
                    context['error'] = 'Користувач з такими даними вже існує!'
                    
                    
    return render(request, 'adding_new_tenant/adding_new_tenant.html')

def log(request):
    context = {}
    
    return render(request, 'adding_new_tenant/log.html', context)