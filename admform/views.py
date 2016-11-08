from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'admform/login.html')
    else:
    	return render(request, 'admform/index.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                # login(request, user)
                # albums = Album.objects.filter(user=request.user)
                return render(request, 'admform/index.html')
            else:
                return render(request, 'admform/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'admform/login.html', {'error_message': 'Invalid login'})
    return render(request, 'admform/login.html')

def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
	    "form": form,
	}
	return render(request, 'admform/login.html', context)
