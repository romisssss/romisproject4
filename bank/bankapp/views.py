from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from bankapp.models import District, AccountType, Branch


def new_page(request):
    return render(request, 'new_page.html')

def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

def userhome(request):
    districts = District.objects.all()
    return render(request, 'userhome.html', {'districts': districts})

def success(request):
    return render(request, 'success.html')

def userform(request):
    districts = District.objects.all()
    account_types = AccountType.objects.all()
    return render(request, 'userform.html', {'districts': districts, 'account_types': account_types})

def get_branches(request, district_id):
    try:
        branches = Branch.objects.filter(district_id=district_id)
        data = {"branches": [{"id": branch.id, "name": branch.name} for branch in branches]}
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:

        form = AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'title': 'Register'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('userform')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:

        form = AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'title': 'Register'})

def submit_form(request):
    if request.method == 'POST':

        return JsonResponse({'message': 'Form submitted successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
def logout(request):
    auth.logout(request)
    return redirect('/')