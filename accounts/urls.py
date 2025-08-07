from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('activate/<uidb64><token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('forgot_password/', views.forgot_password, name = 'forgot_password'),
    path('resetpassword_validate/<uidb64>/<token>', views.resetpassword_validate, name = 'resetpassword_validate'),
    path('reset_password/',views.reset_password, name ='reset_password'),
]