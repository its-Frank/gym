
# from django.urls import path  
# from .views import register, user_login, home, book_appointment, schedule_session  

# urlpatterns = [  
#     path('register/', register, name='register'),  
#     path('login/', user_login, name='login'),  
#     path('book_appointment/', book_appointment, name='book_appointment'),  # Ensure this line exists  
#     path('schedule_session/', schedule_session, name='schedule_session'),  # Ensure this line exists  
#     path('', home, name='home'),  
# ]


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
]