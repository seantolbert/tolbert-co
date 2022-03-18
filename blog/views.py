from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.urls import reverse

from .models import Post

class blog_index(ListView):
    pass