from django.shortcuts import render
from main.models import Blog, Vlog
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def mypage(request):
    user = request.user
    blogs = Blog.objects.filter(writer=user)
    vlogs = Vlog.objects.filter(writer=user) 
    profile = Profile.objects.filter(user=user)
    return render(request, 'users/mypage.html', {'blogs': blogs, 'vlogs': vlogs, 'profile': profile})