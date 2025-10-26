from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

@never_cache
def home(request):
    if request.method == 'POST':
        form = AddExpensesForm(request.POST)
        if form.is_valid():
            print('Form Recieved')
            date = form.cleaned_data['date']
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            user = request.user
            print(date, category, amount)
            Expenses.objects.create(
                date = date,
                category =category,
                amount = amount,
                user = user,
            )
            return redirect('home')
    form = AddExpensesForm()
    expenses = Expenses.objects.all().filter(user=request.user.id)
    print(request.user)
    print(request.user.is_authenticated)
    print(request.user.id)
    return render(request,'index.html', {'form':form, 'expenses':expenses})

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print('Form valid')
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                User.objects.create_user(
                    first_name = f_name,
                    last_name = l_name,
                    email = email,
                    username = email,
                    password = password
                    )
                print('user created')
                user = authenticate(request, username = email, password = password)
                if user is not None:
                    print('logged in')
                    login(request, user)
                    messages.success(request, f'Registered {user}')
                    return redirect('home')
                else:
                    print('User not found ')
            except Exception as e:
                print('error\t',e)
                messages.error(request, e)
                return redirect('register')

        return redirect('home')
    form = CreateUserForm()
    return render(request, 'register.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['email'], password =request.POST['password'])
        if user is not None:
            print('logged in')
            login(request, user)
            messages.success(request, f'Registered {user}')
            return redirect('home')
        else:
            print('User not found ')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Yzou are Logged Out')
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')