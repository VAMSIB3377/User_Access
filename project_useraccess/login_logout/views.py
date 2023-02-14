from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_q_view(request):
    return render(request, 'login_q.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Your account has been disabled."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Invalid login. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')



def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')