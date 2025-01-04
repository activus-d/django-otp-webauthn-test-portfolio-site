from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog

def post_list(request):
    posts = Blog.objects.all().order_by('-publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return render(request, 'blog/home.html')

@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')