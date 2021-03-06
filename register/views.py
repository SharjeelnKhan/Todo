from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


#   def register(request):
# form = CreateUserForm()

"""if request == 'POST':
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

context = {'form': form}
return render(request, 'register/register.html', context)"""


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for ' + user)

        return redirect('login')

    context = {'form': form}
    return render(request, 'register/register.html', context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, 'register/login.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')
