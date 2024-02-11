from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def main(request):
    context = {}
    
    # context['username'] = User.objects.get(username=request.user)
    
    return render(request, 'main_page/main.html', context)