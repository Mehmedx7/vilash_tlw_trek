from django.urls import path
from .import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.Services, name='services'),
    path('packages/', views.Packages, name='packages'),
    path('blogs/', views.Blogs, name='blogs'),
    path('contact/', views.Contact, name='contact'),
    path('register/', views.Register, name='register')
]
