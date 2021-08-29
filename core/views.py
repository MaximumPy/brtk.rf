from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def index (request):

    return render(request, 'core/index.html', {'name': request.GET['name']})