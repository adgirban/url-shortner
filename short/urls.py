from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.create_url, name='create'),
    path('delete/<int:pk>/', views.delete_url, name='delete'),
    path('<str:key>/', views.go, name='go'),
]
