from django import forms  
from .models import Appointment, Session  

class AppointmentForm(forms.ModelForm):  
    class Meta:  
        model = Appointment  
        fields = ['trainer', 'appointment_date', 'notes']  

class SessionForm(forms.ModelForm):  
    class Meta:  
        model = Session  
        fields = ['start_time', 'end_time', 'notes']