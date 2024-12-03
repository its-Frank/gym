# from django.shortcuts import render, redirect  
# from django.contrib.auth import login, authenticate  
# from django.contrib.auth.forms import UserCreationForm  
# from django.contrib.auth.decorators import login_required  
# from .models import Trainer, Appointment, Session  
# from .forms import AppointmentForm, SessionForm  

# def register(request):  
#     if request.method == 'POST':  
#         form = UserCreationForm(request.POST)  
#         if form.is_valid():  
#             user = form.save()  
#             login(request, user)  
#             return redirect('home')  
#     else:  
#         form = UserCreationForm()  
#     return render(request, 'gym/register.html', {'form': form})  

# def user_login(request):  
#     if request.method == 'POST':  
#         username = request.POST['username']  
#         password = request.POST['password']  
#         user = authenticate(request, username=username, password=password)  
#         if user is not None:  
#             login(request, user)  
#             return redirect('home')  
#     return render(request, 'gym/login.html')  

# @login_required  
# def home(request):  
#     return render(request, 'gym/home.html')




# # added
# @login_required  
# def book_appointment(request):  
#     if request.method == 'POST':  
#         form = AppointmentForm(request.POST)  
#         if form.is_valid():  
#             appointment = form.save(commit=False)  
#             appointment.user = request.user  
#             appointment.save()  
#             return redirect('home')  
#     else:  
#         form = AppointmentForm()  
#     return render(request, 'gym/book_appointment.html', {'form': form})  

# @login_required  
# def schedule_session(request):  
#     if request.method == 'POST':  
#         form = SessionForm(request.POST)  
#         if form.is_valid():  
#             session = form.save(commit=False)  
#             session.user = request.user  
#             session.save()  
#             return redirect('home')  
#     else:  
#         form = SessionForm()  
#     return render(request, 'gym/schedule_session.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trainer, Appointment, Session
from .forms import AppointmentForm, SessionForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'gym/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'gym/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def home(request):
    return render(request, 'gym/home.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'gym/book_appointment.html', {'form': form})

@login_required
def schedule_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            messages.success(request, 'Session scheduled successfully!')
            return redirect('home')
    else:
        form = SessionForm()
    return render(request, 'gym/schedule_session.html', {'form': form})