from django.shortcuts import render
from .models import AuthorInfo, Blog

# Create your views here.

def landingPage(request):
    blog = Blog.objects.all()
    context = {
        
        'blog':blog
    }
    return render(request, 'index.html', context)