from django.urls import path

from authapp.views import login, register, logout, edit

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('logout/', logout, name='logout'),

]