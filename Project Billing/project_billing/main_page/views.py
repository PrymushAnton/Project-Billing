from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def main(request):
    context = {}
    

        
        
    
    return render(request, 'main_page/main.html', context)