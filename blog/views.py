from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Post
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class BlogListView(ListView):
    models = Post
    template_name = 'list_post.html'
    context_object_name ='object_list'
    queryset = Post.objects.all()

