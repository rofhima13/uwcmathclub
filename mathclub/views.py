from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mathclub/index.html')

def team(request):
    return render(request, 'mathclub/team.html')

def about(request):
    return render(request, 'mathclub/about.html')

def events(request):
    return render(request, 'mathclub/events.html')

def contact(request):
    return render(request, 'mathclub/contact.html')

def study(request):
    return render(request, 'mathclub/study.html')