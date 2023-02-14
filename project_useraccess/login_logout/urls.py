from django.urls import path
from . import views

#app_name = 'auth'

urlpatterns = [
    path('', views.login_q_view, name='login_q'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
]   