from django.shortcuts import render

def hi(request):
    return render(request, 'events/index.html')