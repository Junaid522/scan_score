from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print("Email: ",email, "Password: ", password)
        return render(request, 'base.html')
    return render(request, 'login.html')

@login_required
def home(requests):
    return render(requests, 'index5.html')

@login_required
def logout(request):
    if request.user.is_authenticated:
        return render( request, 'login.html')

    return render(request, 'base.html')
