from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import*
from django.urls import reverse_lazy
import requests

# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    tempelate_name = 'article_edit.html'

    #Prevents a useer drom being able to edit/update anpther users post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('/')
    
    #Prevents a useer drom being able to delete anpther users post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body', 'author',)
    redirect_field_name = 'account/login/'
    # the currently logged in account can make changes and create post with only his/her account
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#View for anime Quote Api(After sucessful testing)
##