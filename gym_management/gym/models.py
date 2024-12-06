
# from django.db import models  
# from django.contrib.auth.models import User  
# from django.utils import timezone

# class Trainer(models.Model):  
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  
#     specialization = models.CharField(max_length=100)  

#     def __str__(self):  
#         return self.user.username  

# class Trainee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.IntegerField(null=True, blank=True)
#     fitness_goal = models.CharField(max_length=200, blank=True)

#     def __str__(self):  
#         return self.user.username  

# class Appointment(models.Model):  
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)  
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  
#     appointment_date = models.DateTimeField()  
#     notes = models.TextField(blank=True)  

#     def __str__(self):  
#         return f"{self.user.username} - {self.trainer.user.username} on {self.appointment_date}" 


# class Session(models.Model):  
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default=1)  
#     start_time = models.DateTimeField()  
#     end_time = models.DateTimeField()  
#     description = models.TextField(blank=True)  

#     def __str__(self):  
#         return f"Session for {self.user.username} from {self.start_time} to {self.end_time}"
    


# start
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Trainee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    fitness_goal = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):  
    FITNESS_CATEGORIES = [  
        ('yoga', 'Yoga'),  
        ('crossfit', 'Crossfit'),  
        ('cardio', 'Cardio'),  
        ('strength', 'Strength Training'),  
        ('pilates', 'Pilates'),  
        ('zumba', 'Zumba'),  
        ('spinning', 'Spinning'),  
    ]  

    STATUS_CHOICES = [  
        ('pending', 'Pending'),  
        ('accepted', 'Accepted'),  
        ('declined', 'Declined'),  
        ('cancelled', 'Cancelled')  
    ]  

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    appointment_date = models.DateTimeField()  
    notes = models.TextField(blank=True)  
    category = models.CharField(max_length=20, choices=FITNESS_CATEGORIES, default='yoga')  # Default value added here  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  

    def __str__(self):  
        return f"{self.user.username} - {self.trainer.user.username} on {self.appointment_date}"

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default=1)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Session for {self.user.username} from {self.start_time} to {self.end_time}"