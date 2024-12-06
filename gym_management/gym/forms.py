     
from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from .models import Trainer, Trainee, Appointment, Session  

class CustomRegistrationForm(UserCreationForm):  
    ROLE_CHOICES = [  
        ('trainee', 'Trainee'),  
        ('trainer', 'Trainer'),  
    ]  

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)  
    specialization = forms.CharField(  
        max_length=100,   
        required=False,   
        help_text="Required if registering as a trainer"  
    )  
    age = forms.IntegerField(required=False, help_text="Optional for trainees")  
    fitness_goal = forms.CharField(  
        max_length=200,   
        required=False,   
        help_text="Optional for trainees"  
    )  

    class Meta:  
        model = User  
        fields = ['username', 'password1', 'password2', 'role', 'specialization', 'age', 'fitness_goal']  

    def save(self, commit=True):  
        user = super().save(commit=False)  
        if commit:  
            user.save()  
            
            role = self.cleaned_data.get('role')  
            if role == 'trainer':  
                Trainer.objects.create(  
                    user=user,   
                    specialization=self.cleaned_data.get('specialization', '')  
                )  
            elif role == 'trainee':  
                Trainee.objects.create(  
                    user=user,  
                    age=self.cleaned_data.get('age'),  
                    fitness_goal=self.cleaned_data.get('fitness_goal', '')  
                )  
        
        return user  


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['trainer', 'appointment_date', 'category', 'notes']
        
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['trainer', 'start_time', 'end_time', 'description']
        
class ContactForm(forms.Form):  
    name = forms.CharField(max_length=100, required=True)  
    email = forms.EmailField(required=True)  
    message = forms.CharField(widget=forms.Textarea, required=True)


    