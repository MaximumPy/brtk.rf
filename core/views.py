from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post



def index (request):
    return render(request, 'core/index.html')

class BlogListView(ListView):
    model = Post
    template_name = 'nevs.html'