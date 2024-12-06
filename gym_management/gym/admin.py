from django.contrib import admin  
from .models import Trainer, Trainee, Appointment, Session  

# Customizing the Admin interface for Trainer  
class TrainerAdmin(admin.ModelAdmin):  
    list_display = ('user', 'specialization')  
    search_fields = ('user__username', 'specialization')  

# Customizing the Admin interface for Trainee  
class TraineeAdmin(admin.ModelAdmin):  
    list_display = ('user', 'age', 'fitness_goal')  
    search_fields = ('user__username',)  

# Customizing the Admin interface for Appointment  
class AppointmentAdmin(admin.ModelAdmin):  
    list_display = ('user', 'trainer', 'appointment_date', 'notes')  
    search_fields = ('user__username', 'trainer__user__username')  
    list_filter = ('trainer', 'appointment_date')  

# Customizing the Admin interface for Session  
class SessionAdmin(admin.ModelAdmin):  
    list_display = ('user', 'trainer', 'start_time', 'end_time', 'description')  
    search_fields = ('user__username', 'trainer__user__username')  
    list_filter = ('trainer', 'start_time')  

# Registering the models with the admin site  
admin.site.register(Trainer, TrainerAdmin)  
admin.site.register(Trainee, TraineeAdmin)  
admin.site.register(Appointment, AppointmentAdmin)  
admin.site.register(Session, SessionAdmin)
