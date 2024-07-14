from django.shortcuts import render, HttpResponse

# Create your views here.

def experienceView(request):
    return render(request, 'landing/base.html')