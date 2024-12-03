from django.db import models  
from django.contrib.auth.models import User  

class Trainer(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    specialization = models.CharField(max_length=100)  

    def __str__(self):  
        return self.user.username  

class Appointment(models.Model):  
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    appointment_date = models.DateTimeField()  
    notes = models.TextField(blank=True)  

    def __str__(self):  
        return f"{self.user.username} - {self.trainer.user.username} on {self.appointment_date}"  

class Session(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()  
    notes = models.TextField(blank=True)  

    def __str__(self):  
        return f"Session for {self.user.username} from {self.start_time} to {self.end_time}"