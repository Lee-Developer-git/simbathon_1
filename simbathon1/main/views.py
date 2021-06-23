from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .models import Vlog
from django.utils import timezone

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def competition(request):
    vlogs=Vlog.objects.all()
    return render(request, 'competition.html',{'vlogs':vlogs})


def free(request):
    blogs=Blog.objects.all()
    return render(request, 'free.html',{'blogs':blogs})


def detail(request,id): #자유협력 디테일
    blog=get_object_or_404(Blog,pk=id)
    return render(request,'detail.html',{'blog':blog})

def cetail(request,id): #팀원구하기 디테일
    vlog=get_object_or_404(Vlog, pk=id)
    return render(request, 'cetail.html',{'vlog':vlog})

def dnew(request): #자유협력 글쓰기
    return render(request, 'dnew.html')

def dcreate(request):
    dnew_blog=Blog()
    dnew_blog.title=request.POST['title']
    dnew_blog.writer=request.user
    dnew_blog.pub_date=timezone.now()
    dnew_blog.body=request.POST['body']
    dnew_blog.save()
    return redirect('main:detail',dnew_blog.id)

def cnew(request): #팀원구하기 글쓰기
    return render(request, 'cnew.html')

def ccreate(request):
    cnew_vlog=Vlog()
    cnew_vlog.title=request.POST['title']
    cnew_vlog.writer=request.user
    cnew_vlog.pub_date=timezone.now()
    cnew_vlog.body=request.POST['body']
    cnew_vlog.save()
    return redirect('main:cetail',cnew_vlog.id)