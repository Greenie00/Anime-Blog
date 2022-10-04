from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'