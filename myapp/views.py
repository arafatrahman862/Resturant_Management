from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def all_dishes(request):
    return render(request, 'all_dishes.html')

def team_members(request):
    return render(request,'team.html')
