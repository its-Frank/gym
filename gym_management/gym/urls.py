

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('schedule_session/', views.schedule_session, name='schedule_session'),
    path('about/', views.about, name='about'),   
    path('contact/', views.contact, name='contact'),   
    # added
     # New routes  
    path('trainee_dashboard/', views.trainee_dashboard, name='trainee_dashboard'),  
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),  
    path('accept_appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),  
    path('decline_appointment/<int:appointment_id>/', views.decline_appointment, name='decline_appointment'),  
    path('update_session/<int:session_id>/', views.update_session, name='update_session'),  
    path('cancel_session/<int:session_id>/', views.cancel_session, name='cancel_session'),

    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('cancel_trainee_appointment/<int:appointment_id>/', views.cancel_trainee_appointment, name='cancel_trainee_appointment'),
]