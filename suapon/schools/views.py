from django.shortcuts import render

# Create your views here.

def display_web(request):
    return render(request,'child.html')
