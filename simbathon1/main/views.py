from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

def competition(request):
    return render(request, 'competition.html')

def study(request):
    return render(request, 'study.html')

def free(request):
    return render(request, 'free.html')

def volunteer(request):
    return render(request, 'volunteer.html')