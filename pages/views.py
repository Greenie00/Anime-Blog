from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
from articles.models import Article
from .forms import ContactForm

def quotes(request):
    url = "https://anime-quotes1.p.rapidapi.com/api/random"

    headers = {
        "X-RapidAPI-Key": "f15dddb01emsh31ed767ac397d6ep1c0e83jsn2e32396186cb",
        "X-RapidAPI-Host": "anime-quotes1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    context = {'output':response.json}

    return render(request, 'home.html', context)

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = Article.objects.filter(title__icontains=query)
    else:
        data = Article.objects.all()

    context = {'data':data}
    return render(request, 'search.html', context)

def privacy(request):
    return render(request, 'privacy.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect("/")

    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form':form})