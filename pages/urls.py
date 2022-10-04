from django.urls import path
from .views import*
from pages import views

urlpatterns = [
    path('Search/', views.search, name='search'),
    path('Privacy/', views.privacy, name='privacy'),
    path('FAQS/', views.faqs, name='faqs'),
    path('', views.quotes, name='home'),
]