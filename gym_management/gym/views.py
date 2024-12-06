
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Trainer,Trainee, Appointment, Session
from .forms import CustomRegistrationForm, AppointmentForm, SessionForm
from .forms import ContactForm
def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomRegistrationForm()
    return render(request, 'gym/register.html', {'form': form})


def user_login(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            messages.success(request, 'Login successful!')  
            try:
                trainer = Trainer.objects.get(user=user)
                return redirect('trainer_dashboard')  
            except Trainer.DoesNotExist:
                try:
                    trainee = Trainee.objects.get(user=user)
                    return redirect('trainee_dashboard')  
                except Trainee.DoesNotExist:
                    return redirect('home')
        else:  
            messages.error(request, 'Invalid username or password.')  
    return render(request, 'gym/login.html')


def about(request):  
    return render(request, 'gym/about.html')  

def contact(request):  
    return render(request, 'gym/contact.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def home(request):
    return render(request, 'gym/home.html')

@login_required  
def book_appointment(request):  
    available_trainers = Trainer.objects.all()  
    if request.method == 'POST':  
        form = AppointmentForm(request.POST)  
        if form.is_valid():  
            appointment = form.save(commit=False)  
            appointment.user = request.user  
            appointment.status = 'pending'  
            appointment.save()  
            messages.success(request, 'Appointment booked successfully!')  
            return redirect('trainee_dashboard')  
    else:  
        form = AppointmentForm()  
    
    return render(request, 'gym/book_appointment.html', {  
        'form': form,   
        'available_trainers': available_trainers  
    })





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


@login_required  
def trainer_dashboard(request):  
    user = request.user  
    trainer = Trainer.objects.get(user=user)  
    appointments = Appointment.objects.filter(trainer=trainer)  
    sessions = Session.objects.filter(trainer=trainer)  
    context = {  
        'appointments': appointments,  
        'sessions': sessions,  
        'trainer': trainer,  
    }  
    return render(request, 'gym/trainer_dashboard.html', context)


@login_required  
def trainee_dashboard(request):  
    appointments = Appointment.objects.filter(user=request.user)  
    sessions = Session.objects.filter(user=request.user)  
    return render(request, 'gym/trainee_dashboard.html', {  
        'appointments': appointments,  
        'sessions': sessions  
    })  

@login_required
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.user != appointment.user and request.user != appointment.trainer.user:
        messages.error(request, "You are not authorized to view this appointment.")
        return redirect('trainer_dashboard')
    
    context = {
        'appointment': appointment,
    }
    return render(request, 'gym/appointment_details.html', context)


@login_required  
def accept_appointment(request, appointment_id):  
    appointment = Appointment.objects.get(id=appointment_id)  
    appointment.status = 'accepted'  
    appointment.save()   
    return redirect('trainer_dashboard')  

@login_required  
def decline_appointment(request, appointment_id):  
    appointment = Appointment.objects.get(id=appointment_id)  
    appointment.status = 'declined'  
    appointment.save()    
    return redirect('trainer_dashboard')

@login_required  
def update_session(request, session_id):  
    session = Session.objects.get(id=session_id)  
    if request.method == 'POST':  
        form = SessionForm(request.POST, instance=session)  
        if form.is_valid():  
            form.save()   
            return redirect('trainer_dashboard')  
    else:  
        form = SessionForm(instance=session)  
    return render(request, 'gym/update_session.html', {'form': form})

@login_required  
def cancel_appointment(request, appointment_id):  
    appointment = Appointment.objects.get(id=appointment_id)  
    appointment.status = 'cancelled'  
    appointment.save()  
    return redirect('trainer_dashboard')  

@login_required  
def cancel_session(request, session_id):  
    session = Session.objects.get(id=session_id)  
    session.delete()  
    return redirect('trainer_dashboard')


def contact(request):  
    if request.method == 'POST':  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            name = form.cleaned_data['name']  
            email = form.cleaned_data['email']  
            message = form.cleaned_data['message']    
            messages.success(request, 'Thank you for your message! We will get back to you soon.')  
            form = ContactForm() 
    else:  
        form = ContactForm()  
    return render(request, 'gym/contact.html', {'form': form})

# edit appointment
@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully!')
            return redirect('trainee_dashboard')
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'gym/edit_appointment.html', {'form': form})

# cancel trainee appointment
@login_required
def cancel_trainee_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    appointment.status = 'cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully.')
    return redirect('trainee_dashboard')